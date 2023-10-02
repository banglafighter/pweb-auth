from pweb_auth.model.operator_abc import OperatorAbc
from pweb_auth.model.operator_token_abc import OperatorTokenAbc


class PWebAuthConfig:
    OPERATOR_MODEL: OperatorAbc = None
    OPERATOR_TOKEN_MODEL: OperatorTokenAbc = None

    # API End Point
    ENABLE_OPERATOR_API: bool = True
    OPERATOR_API_END_POINT: str = "/api/vi/auth"

    # Form End Point
    ENABLE_SSR_AUTH: bool = False
    SSR_AUTH_END_POINT: str = "/auth"

    # End Point
    LOGIN_END_POINT: str = "/login"
    LOGOUT_END_POINT: str = "/logout"
    RESET_PASS_END_POINT: str = "/reset-password"
    FORGOT_PASS_END_POINT: str = "/forgot-password"
    RENEW_TOKEN_END_POINT: str = "/renew-token"

    # JWT
    JWT_SECRET: str = "PleaseChangeTheToken"
    JWT_REFRESH_TOKEN_VALIDITY_MIN: int = 45
    JWT_ACCESS_TOKEN_VALIDITY_MIN: int = 30
    RESET_PASSWORD_TOKEN_VALID_MIN: int = 150
