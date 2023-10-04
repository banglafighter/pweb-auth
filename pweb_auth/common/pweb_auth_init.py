import pweb_auth.common.pweb_auth_config
from ppy_common import ObjectHelper
from pweb_auth.controller.operator_api_controller import init_operator_api_controller
from pweb_auth.controller.operator_form_controller import init_operator_form_controller
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_auth.form_dto.pweb_auth_dto import OperatorReadDefaultDTO, ForgotPasswordEmailBaseDefaultDTO, \
    ForgotPasswordUsernameBaseDefaultDTO, OperatorCreateEmailBaseDefaultDTO, OperatorUpdateEmailBaseDefaultDTO, \
    OperatorCreateUsernameBaseDefaultDTO, OperatorUpdateUsernameBaseDefaultDTO
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.common.pweb_auth_config import PWebAuthConfig


class PWebAuthInit:

    def register_model(self):
        AuthModel().init()

    def register_controller(self, pweb_app):
        if PWebAuthConfig.ENABLE_OPERATOR_API:
            api_controller = init_operator_api_controller(url_prefix=PWebAuthConfig.OPERATOR_API_END_POINT)
            pweb_app.register_blueprint(api_controller)

        if PWebAuthConfig.ENABLE_SSR_AUTH:
            form_controller = init_operator_form_controller(url_prefix=PWebAuthConfig.SSR_AUTH_END_POINT)
            pweb_app.register_blueprint(form_controller)

    def _select_dto_by_system_auth_base(self, username_base, email_base):
        if PWebAuthConfig.SYSTEM_AUTH_BASE == AuthBase.USERNAME:
            return username_base
        return email_base

    def merge_auth_config(self):
        if not PWebAuthConfig.OPERATOR_READ_DTO:
            PWebAuthConfig.OPERATOR_READ_DTO = OperatorReadDefaultDTO()

        if not PWebAuthConfig.LOGIN_RESPONSE_DTO:
            PWebAuthConfig.LOGIN_RESPONSE_DTO = PWebAuthConfig.OPERATOR_READ_DTO

        if not PWebAuthConfig.FORGOT_PASSWORD_DTO:
            PWebAuthConfig.FORGOT_PASSWORD_DTO = self._select_dto_by_system_auth_base(username_base=ForgotPasswordUsernameBaseDefaultDTO(), email_base=ForgotPasswordEmailBaseDefaultDTO())

        if not PWebAuthConfig.OPERATOR_CREATE_DTO:
            PWebAuthConfig.OPERATOR_CREATE_DTO = self._select_dto_by_system_auth_base(username_base=OperatorCreateUsernameBaseDefaultDTO(), email_base=OperatorCreateEmailBaseDefaultDTO())

        if not PWebAuthConfig.OPERATOR_UPDATE_DTO:
            PWebAuthConfig.OPERATOR_UPDATE_DTO = self._select_dto_by_system_auth_base(username_base=OperatorUpdateUsernameBaseDefaultDTO(), email_base=OperatorUpdateEmailBaseDefaultDTO())

    def merge_config(self, config):
        ObjectHelper.copy_config_property(config, pweb_auth.common.pweb_auth_config.PWebAuthConfig)
        self.merge_auth_config()

    def init(self, pweb_app, config):
        self.merge_config(config=config)
        self.register_model()
        self.register_controller(pweb_app=pweb_app)
