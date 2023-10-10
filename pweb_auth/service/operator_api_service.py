from ppy_common import PyCommon, DataUtil
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.common.pweb_auth_util import PWebAuthUtil
from pweb_auth.form_dto.pweb_auth_dto import ResetPasswordDefaultDTO, RefreshTokenDefaultDTO
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.security.pweb_jwt import PWebJWT
from pweb_auth.service.operator_service import OperatorService
from pweb_form_rest import RESTDataCRUD, form_rest_exception
from pweb_form_rest.data.pweb_response_status import PWebResponseCode


class OperatorAPIService:
    operator_service = OperatorService()
    rest_data_crud: RESTDataCRUD = None
    pweb_jwt: PWebJWT = PWebJWT()
    OPERATOR = "operator"
    TOKEN = "token"

    def get_operator_token_by_operator_id(self, operator_id):
        return AuthModel.operatorToken.query.filter(AuthModel.operatorToken.tokenOwnerId == operator_id).first()

    def get_operator_token_by_token(self, token):
        return AuthModel.operatorToken.query.filter(AuthModel.operatorToken.token == token).first()

    def get_access_token(self, operator_id, payload: dict = None):
        operator = self.operator_service.get_operator_by_id(operator_id)
        if not operator:
            return None

        if not payload:
            payload = {}
        payload[self.OPERATOR] = operator.id
        return self.pweb_jwt.get_access_token(payload, iss=operator.uuid)

    def create_or_update_db_refresh_token(self, operator_id, uuid=None):
        existing_token = self.get_operator_token_by_operator_id(operator_id)
        if uuid and (not existing_token or existing_token.token != uuid):
            return None

        if not existing_token:
            existing_token = AuthModel.operatorToken(name=PWebAuthConfig.REFRESH_TOKEN_NAME, tokenOwnerId=operator_id)

        existing_token.token = PyCommon.uuid()
        existing_token.save()
        return existing_token

    def get_refresh_token(self, operator_id, payload: dict = None):
        operator = self.operator_service.get_operator_by_id(operator_id)
        if not operator:
            return None
        if not payload:
            payload = {}
        payload[self.OPERATOR] = operator.id
        db_token = self.create_or_update_db_refresh_token(operator_id)
        if not db_token:
            return None
        payload[self.TOKEN] = db_token.token
        return self.pweb_jwt.get_refresh_token(payload, iss=operator.uuid)

    def process_login_response(self, operator):
        token = {
            "accessToken": self.get_access_token(operator_id=operator.id),
            "refreshToken": self.get_refresh_token(operator_id=operator.id)
        }
        response = {
            "operator": operator,
            "token": token
        }
        response_dict = PWebAuthConfig.LOGIN_RESPONSE_DTO().dump(response)

        on_token_generation = PWebAuthUtil.on_token_generation()
        if on_token_generation:
            response = on_token_generation.perform(response=response_dict, operator=operator)
            if response:
                return response
        return self.rest_data_crud.response_maker.dictionary_object_response(data=response_dict)

    def login(self):
        data = self.rest_data_crud.get_json_data(PWebAuthConfig.LOGIN_DTO())
        operator = self.operator_service.login(login_data=data)
        return self.process_login_response(operator=operator)

    def logout(self):
        return self.rest_data_crud.response_maker.success_message(message=PWebAuthConfig.LOGOUT_SUCCESS_SM)

    def renew_token_by_refresh_token(self, token):
        jwt_payload = self.pweb_jwt.validate_token(token)
        if not jwt_payload:
            raise form_rest_exception.error_message_exception(PWebAuthConfig.INVALID_TOKEN_SM, PWebResponseCode.invalid_token_code)

        if self.TOKEN not in jwt_payload or self.OPERATOR not in jwt_payload:
            raise form_rest_exception.error_message_exception(PWebAuthConfig.INVALID_TOKEN_SM, PWebResponseCode.invalid_token_code)

        operator_token = self.get_operator_token_by_token(jwt_payload[self.TOKEN])
        operator_id = jwt_payload[self.OPERATOR]
        if not operator_token:
            raise form_rest_exception.error_message_exception(PWebAuthConfig.TOKEN_EXPIRED_SM, PWebResponseCode.token_expired_code)

        access_token = self.get_access_token(operator_id)
        refresh_token = self.get_refresh_token(operator_id)
        if not access_token or not refresh_token:
            raise form_rest_exception.error_message_exception(PWebAuthConfig.TOKEN_GENERATION_ERROR_SM, PWebResponseCode.token_error_code)

        token = {
            "accessToken": access_token,
            "refreshToken": refresh_token
        }

        on_renew_token = PWebAuthUtil.on_renew_token()
        if on_renew_token:
            response = on_renew_token.perform(token=token, jwt_payload=jwt_payload)
            if response:
                return response
        return self.rest_data_crud.response_maker.dictionary_object_response(data=token)

    def renew_token(self):
        data = self.rest_data_crud.get_json_data(RefreshTokenDefaultDTO())
        response = self.renew_token_by_refresh_token(data["refreshToken"])
        return response

    def reset_password(self):
        data = self.rest_data_crud.get_json_data(ResetPasswordDefaultDTO())
        token = DataUtil.get_dict_value(data, "token")
        new_password = DataUtil.get_dict_value(data, "newPassword")
        is_reset = self.operator_service.set_password_by_token(token=token, new_password=new_password)
        if is_reset:
            self.rest_data_crud.response_maker.success_message(message=PWebAuthConfig.SUCCESSFULLY_RESET_PASSWORD_SM)
        return self.rest_data_crud.response_maker.error_message(message=PWebAuthConfig.UNABLE_TO_RESET_PASSWORD_SM)

    def forgot_password(self):
        data = self.rest_data_crud.get_json_data(PWebAuthConfig.FORGOT_PASSWORD_DTO())
        self.operator_service.forgot_password(password_request=data)
        return self.rest_data_crud.response_maker.success_message(message=PWebAuthConfig.PASS_RESET_REQUEST_SEND_SM)
