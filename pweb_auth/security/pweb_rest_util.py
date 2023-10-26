from pweb_auth.security.pweb_jwt import PWebJWT
from pweb_form_rest.crud.pweb_request_data import RequestData


class PWebRESTUtil:
    request_data = RequestData()
    pweb_jwt = PWebJWT()

    @staticmethod
    def get_api_auth_data():
        bearer_token = PWebRESTUtil.request_data.get_bearer_token()
        return PWebRESTUtil.pweb_jwt.validate_token(bearer_token)
