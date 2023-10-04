from pweb_auth.common.pweb_auth_interceptor import PWebAuthInterceptor
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_auth.model.operator_abc import OperatorAbc
from pweb_auth.model.operator_token_abc import OperatorTokenAbc
from pweb_form_rest.schema.pweb_rest_schema import PWebRestDTO


class PWebAuthConfig:
    OPERATOR_MODEL: OperatorAbc = None
    OPERATOR_TOKEN_MODEL: OperatorTokenAbc = None

    # JWT
    JWT_SECRET: str = "PleaseChangeTheToken"
    JWT_REFRESH_TOKEN_VALIDITY_MIN: int = 45
    JWT_ACCESS_TOKEN_VALIDITY_MIN: int = 30
    RESET_PASSWORD_TOKEN_VALID_MIN: int = 150

    # Auth
    SYSTEM_AUTH_BASE: AuthBase = AuthBase.EMAIL
    LOGIN_RESPONSE_DTO: PWebRestDTO = None
    FORGOT_PASSWORD_DTO: PWebRestDTO = None
    OPERATOR_CREATE_DTO: PWebRestDTO = None
    OPERATOR_UPDATE_DTO: PWebRestDTO = None
    OPERATOR_READ_DTO: PWebRestDTO = None

    AUTH_INTERCEPTOR: PWebAuthInterceptor = None
