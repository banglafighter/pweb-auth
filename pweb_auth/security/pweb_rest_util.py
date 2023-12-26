from pweb_form_rest import form_rest_exception
from pweb_auth.security.pweb_jwt import PWebJWT
from pweb_form_rest.crud.pweb_request_data import RequestData


class PWebRESTUtil:
    request_data = RequestData()
    pweb_jwt = PWebJWT()

    @staticmethod
    def get_api_auth_data():
        bearer_token = PWebRESTUtil.request_data.get_bearer_token()
        return PWebRESTUtil.pweb_jwt.validate_token(bearer_token)

    @staticmethod
    def get_operator_id_from_payload(error_message="Invalid operator", payload=None):
        if not payload:
            payload = PWebRESTUtil.get_api_auth_data()
        if not payload or "operator" not in payload:
            raise form_rest_exception.error_message_exception(error_message)
        return payload['operator']

