from pweb_auth.common.pweb_auth_interceptor_abc import PWebAuthInterceptOnLogin, PWebAuthCustomLogin, \
    PWebAuthInterceptOnACLCheck, PWebAuthInterceptOnTokenGeneration, PWebAuthInterceptOnRenewToken, \
    PWebAuthBaseInterceptor, PWebAuthSkipURLChecker
from pweb_auth.common.pweb_auth_notify_abc import PWebAuthNotifyOnForgotPasswordRequest, \
    PWebAuthNotifyOnResetPasswordFailed, PWebAuthNotifyOnResetPasswordSuccess, PWebAuthNotifyOnLoginFailed, \
    PWebAuthNotifyOnLoginSuccess, PWebAuthNotifyOnCreateOperator
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
    LOGIN_DTO: PWebRestDTO = None
    LOGIN_RESPONSE_DTO: PWebRestDTO = None
    FORGOT_PASSWORD_DTO: PWebRestDTO = None
    OPERATOR_CREATE_DTO: PWebRestDTO = None
    OPERATOR_UPDATE_DTO: PWebRestDTO = None
    OPERATOR_READ_DTO: PWebRestDTO = None

    # Auth Interceptors
    IS_ENABLE_AUTH: bool = True
    SSR_UNAUTHORIZED_REDIRECT_URL = "/auth/login"
    REST_URL_START_WITH = "api"
    REFRESH_TOKEN_NAME = "REFRESH_TOKEN"
    SKIP_URL_FROM_AUTH: list = []
    SKIP_START_WITH_URL_FROM_AUTH: list = []
    AUTH_SKIP_URL_CHECKER: PWebAuthSkipURLChecker = None
    AUTH_INTERCEPTOR: PWebAuthBaseInterceptor = None
    AUTH_INTERCEPT_ON_LOGIN: PWebAuthInterceptOnLogin = None
    AUTH_CUSTOM_LOGIN: PWebAuthCustomLogin = None
    AUTH_INTERCEPT_ON_ACL_CHECK: PWebAuthInterceptOnACLCheck = None
    AUTH_INTERCEPT_ON_TOKEN_GENERATION: PWebAuthInterceptOnTokenGeneration = None
    AUTH_INTERCEPT_ON_RENEW_TOKEN: PWebAuthInterceptOnRenewToken = None

    # Auth Notification
    AUTH_NOTIFY_ON_FORGOT_PASSWORD_REQUEST: PWebAuthNotifyOnForgotPasswordRequest = None
    AUTH_NOTIFY_ON_RESET_PASSWORD_FAILED: PWebAuthNotifyOnResetPasswordFailed = None
    AUTH_NOTIFY_ON_RESET_PASSWORD_SUCCESS: PWebAuthNotifyOnResetPasswordSuccess = None
    AUTH_NOTIFY_ON_LOGIN_FAILED: PWebAuthNotifyOnLoginFailed = None
    AUTH_NOTIFY_ON_LOGIN_SUCCESS: PWebAuthNotifyOnLoginSuccess = None
    AUTH_NOTIFY_ON_CREATE_OPERATOR: PWebAuthNotifyOnCreateOperator = None

    # Messages
    INVALID_CREDENTIALS_SM = "Invalid Credentials! Please enter valid Credential"
    ACCOUNT_NOT_VERIFIED_SM = "Sorry your account has not been verified."
    NOT_AUTHORIZE_SM = "You are not Authorize for Access."
    LOGIN_FIRST_SM = "Please login before accessing restricted content"
    CHECK_VALIDATION_ERROR_SM = "Please check the validation error"
    UNABLE_PROCESS_LOGIN_SM = "Please check your data. Unable to process login"
    PASS_RESET_REQUEST_SEND_SM = "Password Reset Request Send"
    SUCCESSFULLY_RESET_PASSWORD_SM = "Successfully Password Reset!"
    UNABLE_TO_RESET_PASSWORD_SM = "Unable to reset password"
    INVALID_TOKEN_SM = "Invalid Token"
    TOKEN_EXPIRED_SM = "Token Expired"
    TOKEN_GENERATION_ERROR_SM = "Unable to generate token"
    LOGOUT_SUCCESS_SM = "Successfully Logout"
