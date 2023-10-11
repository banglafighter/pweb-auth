from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.common.pweb_auth_interceptor_abc import PWebAuthCustomLogin, PWebAuthInterceptOnLogin, \
    PWebAuthInterceptOnACLCheck, PWebAuthInterceptOnTokenGeneration, PWebAuthInterceptOnRenewToken, \
    PWebAuthSkipURLChecker
from pweb_auth.common.pweb_auth_notify_abc import PWebAuthNotifyOnForgotPasswordRequest, \
    PWebAuthNotifyOnResetPasswordFailed, PWebAuthNotifyOnResetPasswordSuccess, PWebAuthNotifyOnLoginFailed, \
    PWebAuthNotifyOnLoginSuccess, PWebAuthNotifyOnCreateOperator


class PWebAuthUtil:

    @staticmethod
    def skip_url_checker() -> PWebAuthSkipURLChecker | None:
        if PWebAuthConfig.AUTH_SKIP_URL_CHECKER and isinstance(PWebAuthConfig.AUTH_SKIP_URL_CHECKER, PWebAuthSkipURLChecker):
            return PWebAuthConfig.AUTH_SKIP_URL_CHECKER
        return None

    @staticmethod
    def custom_login() -> PWebAuthCustomLogin | None:
        if PWebAuthConfig.AUTH_CUSTOM_LOGIN and isinstance(PWebAuthConfig.AUTH_CUSTOM_LOGIN, PWebAuthCustomLogin):
            return PWebAuthConfig.AUTH_CUSTOM_LOGIN
        return None

    @staticmethod
    def on_login() -> PWebAuthInterceptOnLogin | None:
        if PWebAuthConfig.AUTH_INTERCEPT_ON_LOGIN and isinstance(PWebAuthConfig.AUTH_INTERCEPT_ON_LOGIN, PWebAuthInterceptOnLogin):
            return PWebAuthConfig.AUTH_INTERCEPT_ON_LOGIN
        return None

    @staticmethod
    def on_acl_check() -> PWebAuthInterceptOnACLCheck | None:
        if PWebAuthConfig.AUTH_INTERCEPT_ON_ACL_CHECK and isinstance(PWebAuthConfig.AUTH_INTERCEPT_ON_ACL_CHECK, PWebAuthInterceptOnACLCheck):
            return PWebAuthConfig.AUTH_INTERCEPT_ON_ACL_CHECK
        return None

    @staticmethod
    def on_token_generation() -> PWebAuthInterceptOnTokenGeneration | None:
        if PWebAuthConfig.AUTH_INTERCEPT_ON_TOKEN_GENERATION and isinstance(PWebAuthConfig.AUTH_INTERCEPT_ON_TOKEN_GENERATION, PWebAuthInterceptOnTokenGeneration):
            return PWebAuthConfig.AUTH_INTERCEPT_ON_TOKEN_GENERATION
        return None

    @staticmethod
    def on_renew_token() -> PWebAuthInterceptOnRenewToken | None:
        if PWebAuthConfig.AUTH_INTERCEPT_ON_RENEW_TOKEN and isinstance(PWebAuthConfig.AUTH_INTERCEPT_ON_RENEW_TOKEN, PWebAuthInterceptOnRenewToken):
            return PWebAuthConfig.AUTH_INTERCEPT_ON_RENEW_TOKEN
        return None

    @staticmethod
    def notify_on_forgot_password_request() -> PWebAuthNotifyOnForgotPasswordRequest | None:
        if PWebAuthConfig.AUTH_NOTIFY_ON_FORGOT_PASSWORD_REQUEST and isinstance(PWebAuthConfig.AUTH_NOTIFY_ON_FORGOT_PASSWORD_REQUEST, PWebAuthNotifyOnForgotPasswordRequest):
            return PWebAuthConfig.AUTH_NOTIFY_ON_FORGOT_PASSWORD_REQUEST
        return None

    @staticmethod
    def notify_on_reset_password_failed() -> PWebAuthNotifyOnResetPasswordFailed | None:
        if PWebAuthConfig.AUTH_NOTIFY_ON_RESET_PASSWORD_FAILED and isinstance(PWebAuthConfig.AUTH_NOTIFY_ON_RESET_PASSWORD_FAILED, PWebAuthNotifyOnResetPasswordFailed):
            return PWebAuthConfig.AUTH_NOTIFY_ON_RESET_PASSWORD_FAILED
        return None

    @staticmethod
    def notify_on_reset_password_success() -> PWebAuthNotifyOnResetPasswordSuccess | None:
        if PWebAuthConfig.AUTH_NOTIFY_ON_RESET_PASSWORD_SUCCESS and isinstance(PWebAuthConfig.AUTH_NOTIFY_ON_RESET_PASSWORD_SUCCESS, PWebAuthNotifyOnResetPasswordSuccess):
            return PWebAuthConfig.AUTH_NOTIFY_ON_RESET_PASSWORD_SUCCESS
        return None

    @staticmethod
    def notify_on_login_failed() -> PWebAuthNotifyOnLoginFailed | None:
        if PWebAuthConfig.AUTH_NOTIFY_ON_LOGIN_FAILED and isinstance(PWebAuthConfig.AUTH_NOTIFY_ON_LOGIN_FAILED, PWebAuthNotifyOnLoginFailed):
            return PWebAuthConfig.AUTH_NOTIFY_ON_LOGIN_FAILED
        return None

    @staticmethod
    def notify_on_login_success() -> PWebAuthNotifyOnLoginSuccess | None:
        if PWebAuthConfig.AUTH_NOTIFY_ON_LOGIN_SUCCESS and isinstance(PWebAuthConfig.AUTH_NOTIFY_ON_LOGIN_SUCCESS, PWebAuthNotifyOnLoginSuccess):
            return PWebAuthConfig.AUTH_NOTIFY_ON_LOGIN_SUCCESS
        return None

    @staticmethod
    def notify_on_create_operator() -> PWebAuthNotifyOnCreateOperator | None:
        if PWebAuthConfig.AUTH_NOTIFY_ON_CREATE_OPERATOR and isinstance(PWebAuthConfig.AUTH_NOTIFY_ON_CREATE_OPERATOR, PWebAuthNotifyOnCreateOperator):
            return PWebAuthConfig.AUTH_NOTIFY_ON_CREATE_OPERATOR
        return None
