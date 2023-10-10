from ppy_common import PyCommon
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.security.pweb_jwt import PWebJWT
from pweb_auth.service.operator_service import OperatorService
from pweb_form_rest import RESTDataCRUD


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
        return self.rest_data_crud.response_maker.dictionary_object_response(data=response_dict)

    def login(self):
        data = self.rest_data_crud.get_json_data(PWebAuthConfig.LOGIN_DTO())
        operator = self.operator_service.login(login_data=data)
        return self.process_login_response(operator=operator)

    def logout(self):
        pass

    def reset_password(self):
        pass

    def forgot_password(self):
        pass
