from ppy_common import DataUtil
from pweb_auth.common.pweb_auth_util import PWebAuthUtil
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_form_rest import form_rest_exception


class OperatorService:

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

    def get_operator_by_token(self, token):
        return AuthModel.operator.query.filter(AuthModel.operator.token == token, AuthModel.operator.isDeleted == False).first()

    def get_operator_by_login_data(self, login_data: dict):
        auth_base = PWebAuthConfig.SYSTEM_AUTH_BASE
        if auth_base == AuthBase.EMAIL:
            email = DataUtil.get_dict_value(login_data, "email")
            return self.get_operator_by_email(email)
        elif auth_base == AuthBase.USERNAME:
            username = DataUtil.get_dict_value(login_data, "username")
            return self.get_operator_by_username(username)
        return None

    def validate_password_and_get_operator(self, login_data: dict):
        password = DataUtil.get_dict_value(login_data, "password")
        if not password:
            return None
        operator = self.get_operator_by_login_data(login_data=login_data)
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
