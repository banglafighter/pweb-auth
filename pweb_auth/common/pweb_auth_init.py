import pweb_auth.common.pweb_auth_config
from ppy_common import ObjectHelper
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_auth.form_dto.pweb_auth_dto import OperatorReadDefaultDTO, ForgotPasswordEmailBaseDefaultDTO, \
    ForgotPasswordUsernameBaseDefaultDTO, OperatorCreateEmailBaseDefaultDTO, OperatorUpdateEmailBaseDefaultDTO, \
    OperatorCreateUsernameBaseDefaultDTO, OperatorUpdateUsernameBaseDefaultDTO
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.common.pweb_auth_config import PWebAuthConfig


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
            PWebAuthConfig.LOGIN_RESPONSE_DTO = PWebAuthConfig.OPERATOR_READ_DTO

        if not PWebAuthConfig.FORGOT_PASSWORD_DTO:
            PWebAuthConfig.FORGOT_PASSWORD_DTO = self._select_dto_by_system_auth_base(username_base=ForgotPasswordUsernameBaseDefaultDTO, email_base=ForgotPasswordEmailBaseDefaultDTO)

        self.init_create_operator_dto()
        self.init_update_operator_dto()

    def merge_config(self, config):
        ObjectHelper.copy_config_property(config, pweb_auth.common.pweb_auth_config.PWebAuthConfig)

    def init(self, pweb_app, config):
        self.merge_config(config=config)
        self.register_model()
        self.merge_auth_config()
