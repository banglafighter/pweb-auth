from ppy_common import DataUtil, PyCommon
from pweb_auth.common.pweb_auth_util import PWebAuthUtil
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_auth.security.pweb_jwt import PWebJWT
from pweb_form_rest import form_rest_exception


class OperatorService:
    pweb_jwt: PWebJWT = PWebJWT()

    def is_username_available(self, username: str, model_id: int = None):
        operator = AuthModel.operator.query.filter(AuthModel.operator.username == username).first()
        if operator:
            if model_id and operator.id == model_id:
                return True
            return False
        return True

    def is_email_available(self, email: str, model_id: int = None):
        operator = AuthModel.operator.query.filter(AuthModel.operator.email == email).first()
        if operator:
            if model_id and operator.id == model_id:
                return True
            return False
        return True

    def is_operator_integrity_broken(self, request_data: dict, model_id: int):
        auth_base = PWebAuthConfig.SYSTEM_AUTH_BASE
        is_broken_integrity = True
        if auth_base == AuthBase.EMAIL:
            email = DataUtil.get_dict_value(request_data, "email")
            is_broken_integrity = not self.is_email_available(email=email, model_id=model_id)
        elif auth_base == AuthBase.USERNAME:
            username = DataUtil.get_dict_value(request_data, "username")
            is_broken_integrity = not self.is_username_available(username=username, model_id=model_id)
        return is_broken_integrity

    def get_operator_by_email(self, email):
        return AuthModel.operator.query.filter(AuthModel.operator.email == email, AuthModel.operator.isDeleted == False).first()

    def get_operator_by_username(self, username):
        return AuthModel.operator.query.filter(AuthModel.operator.username == username, AuthModel.operator.isDeleted == False).first()

    def get_operator_by_id(self, model_id):
        return AuthModel.operator.query.filter(AuthModel.operator.id == model_id, AuthModel.operator.isDeleted == False).first()

    def get_operator_by_token(self, token):
        return AuthModel.operator.query.filter(AuthModel.operator.token == token, AuthModel.operator.isDeleted == False).first()


    def get_operator_by_dict_data(self, dict_data: dict):
        auth_base = PWebAuthConfig.SYSTEM_AUTH_BASE
        if auth_base == AuthBase.EMAIL:
            email = DataUtil.get_dict_value(dict_data, "email")
            return self.get_operator_by_email(email)
        elif auth_base == AuthBase.USERNAME:
            username = DataUtil.get_dict_value(dict_data, "username")
            return self.get_operator_by_username(username)
        return None

    def validate_password_and_get_operator(self, login_data: dict):
        password = DataUtil.get_dict_value(login_data, "password")
        if not password:
            return None
        operator = self.get_operator_by_dict_data(dict_data=login_data)
        if operator and operator.verify_password(password):
            return operator
        return None

    def notify_on_login_failed(self, operator, login_data: dict):
        notify_on_login_failed = PWebAuthUtil.notify_on_login_failed()
        if notify_on_login_failed:
            notify_on_login_failed.perform(operator=operator, login_data=login_data)

    def intercept_login_data(self, operator, login_data: dict):
        on_login = PWebAuthUtil.on_login()
        if not operator:
            self.notify_on_login_failed(operator=operator, login_data=login_data)
            raise form_rest_exception.error_message_exception(message=PWebAuthConfig.INVALID_CREDENTIALS_SM)
        elif not operator.isVerified:
            raise form_rest_exception.error_message_exception(message=PWebAuthConfig.ACCOUNT_NOT_VERIFIED_SM)

        if on_login:
            response = on_login.perform(operator=operator, login_data=login_data)
            if response:
                return response

        notify_on_login_success = PWebAuthUtil.notify_on_login_success()
        if notify_on_login_success:
            notify_on_login_success.perform(operator=operator, login_data=login_data)

        return operator

    def login(self, login_data: dict):
        custom_login = PWebAuthUtil.custom_login()
        if custom_login:
            operator = custom_login.perform(login_data=login_data)
        else:
            operator = self.validate_password_and_get_operator(login_data=login_data)
        return self.intercept_login_data(operator=operator, login_data=login_data)

    def forgot_password(self, password_request: dict):
        operator = self.get_operator_by_dict_data(dict_data=password_request)
        if not operator:
            return False

        operator.token = PyCommon.get_random() + str(operator.id)
        validity = self.pweb_jwt.get_token_validity(PWebAuthConfig.RESET_PASSWORD_TOKEN_VALID_MIN)
        token = self.pweb_jwt.get_token(validity, {"token": operator.token})
        operator.save()

        forgot_password_request = PWebAuthUtil.notify_on_forgot_password_request()
        if forgot_password_request:
            return forgot_password_request.perform(operator=operator, reset_token=token)
        return False

    def set_password_by_token(self, token: str, new_password: str):
        payload = self.pweb_jwt.validate_token(token)
        if payload and "token" in payload:
            reset_password_success = PWebAuthUtil.notify_on_reset_password_success()
            operator = self.get_operator_by_token(payload["token"])
            if operator:
                operator.password = new_password
                operator.token = None
                operator.save()
                if reset_password_success:
                    reset_password_success.perform(operator=operator)
                return True
        reset_password_failed = PWebAuthUtil.notify_on_reset_password_failed()
        if reset_password_failed:
            reset_password_failed.perform(reset_token=token)
        return False

    def admin_reset_password(self, operator_id, password):
        operator = self.get_operator_by_id(model_id=operator_id)
        if not operator:
            return False
        operator.password = password
        operator.save()
        return True

    def change_password(self, operator_id, current_password, new_password):
        operator = self.get_operator_by_id(model_id=operator_id)
        if not operator:
            return False

        if not operator.verify_password(current_password):
            return False

        operator.password = new_password
        operator.save()
        return True
