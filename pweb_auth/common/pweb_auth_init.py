import pweb_auth.common.pweb_auth_config
from ppy_common import ObjectHelper
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_auth.data.pweb_auth_registry import PWebAuthRegistry
from pweb_auth.form_dto.pweb_auth_dto import OperatorReadDefaultDTO, ForgotPasswordEmailBaseDefaultDTO, \
    ForgotPasswordUsernameBaseDefaultDTO, OperatorCreateEmailBaseDefaultDTO, OperatorUpdateEmailBaseDefaultDTO, \
    OperatorCreateUsernameBaseDefaultDTO, OperatorUpdateUsernameBaseDefaultDTO, LoginUsernameBaseDefaultDTO, \
    LoginEmailBaseDefaultDTO, LoginResponseDefaultDTO
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.security.pweb_auth_interceptor import PWebAuthInterceptor
from pweb_auth.service.operator_api_service import OperatorAPIService
from pweb_auth.service.operator_ssr_service import OperatorSSRService
from pweb_form_rest import RESTDataCRUD
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class PWebAuthInit:

    def register_model(self):
        AuthModel().init()

    def _select_dto_by_system_auth_base(self, username_base, email_base):
        if PWebAuthConfig.SYSTEM_AUTH_BASE == AuthBase.USERNAME:
            return username_base
        return email_base

    def init_create_operator_dto(self):
        if PWebAuthConfig.OPERATOR_CREATE_DTO:
            return

        _OperatorCreateDTO = self._select_dto_by_system_auth_base(username_base=OperatorCreateUsernameBaseDefaultDTO, email_base=OperatorCreateEmailBaseDefaultDTO)

        class OperatorCreateDTO(_OperatorCreateDTO):
            class Meta:
                model = PWebAuthConfig.OPERATOR_MODEL
                load_instance = True

        PWebAuthConfig.OPERATOR_CREATE_DTO = OperatorCreateDTO

    def init_update_operator_dto(self):
        if PWebAuthConfig.OPERATOR_UPDATE_DTO:
            return

        _OperatorUpdateDTO = self._select_dto_by_system_auth_base(username_base=OperatorUpdateUsernameBaseDefaultDTO, email_base=OperatorUpdateEmailBaseDefaultDTO)

        class OperatorUpdateDTO(_OperatorUpdateDTO):
            class Meta:
                model = PWebAuthConfig.OPERATOR_MODEL
                load_instance = True

        PWebAuthConfig.OPERATOR_UPDATE_DTO = OperatorUpdateDTO

    def merge_auth_config(self):
        if not PWebAuthConfig.OPERATOR_READ_DTO:
            PWebAuthConfig.OPERATOR_READ_DTO = OperatorReadDefaultDTO

        if not PWebAuthConfig.LOGIN_RESPONSE_DTO:
            PWebAuthConfig.LOGIN_RESPONSE_DTO = LoginResponseDefaultDTO

        if not PWebAuthConfig.LOGIN_DTO:
            PWebAuthConfig.LOGIN_DTO = self._select_dto_by_system_auth_base(username_base=LoginUsernameBaseDefaultDTO, email_base=LoginEmailBaseDefaultDTO)

        if not PWebAuthConfig.FORGOT_PASSWORD_DTO:
            PWebAuthConfig.FORGOT_PASSWORD_DTO = self._select_dto_by_system_auth_base(username_base=ForgotPasswordUsernameBaseDefaultDTO, email_base=ForgotPasswordEmailBaseDefaultDTO)

        self.init_create_operator_dto()
        self.init_update_operator_dto()

    def merge_config(self, config):
        ObjectHelper.copy_config_property(config, pweb_auth.common.pweb_auth_config.PWebAuthConfig)

    def init_service_dependencies(self):
        OperatorSSRService.form_data_crud = FormDataCRUD(model=PWebAuthConfig.OPERATOR_MODEL)
        OperatorAPIService.rest_data_crud = RESTDataCRUD(model=PWebAuthConfig.OPERATOR_MODEL)

    def init_auth_interceptor(self, pweb_app):
        if not PWebAuthConfig.IS_ENABLE_AUTH or not pweb_app:
            return

        if not PWebAuthConfig.AUTH_INTERCEPTOR or not isinstance(PWebAuthConfig.AUTH_INTERCEPTOR, PWebAuthInterceptor):
            PWebAuthConfig.AUTH_INTERCEPTOR = PWebAuthInterceptor()

        if PWebAuthConfig.SKIP_START_WITH_URL_FROM_AUTH and isinstance(PWebAuthConfig.SKIP_START_WITH_URL_FROM_AUTH, list):
            PWebAuthRegistry.add_start_with_url_list_in_skip(PWebAuthConfig.SKIP_START_WITH_URL_FROM_AUTH)

        if PWebAuthConfig.SKIP_URL_FROM_AUTH and isinstance(PWebAuthConfig.SKIP_URL_FROM_AUTH, list):
            PWebAuthRegistry.add_url_list_in_skip(PWebAuthConfig.SKIP_URL_FROM_AUTH)

        PWebAuthRegistry.add_url_in_skip(PWebAuthConfig.SSR_UNAUTHORIZED_REDIRECT_URL)
        pweb_app.before_request_funcs.setdefault(None, []).append(PWebAuthConfig.AUTH_INTERCEPTOR.intercept)

    def init(self, pweb_app, config):
        self.merge_config(config=config)
        self.register_model()
        self.merge_auth_config()
        self.init_service_dependencies()
        self.init_auth_interceptor(pweb_app=pweb_app)
