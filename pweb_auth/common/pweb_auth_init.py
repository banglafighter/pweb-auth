import pweb_auth.common.pweb_auth_config
from ppy_common import ObjectHelper
from pweb_auth.controller.operator_api_controller import init_operator_api_controller
from pweb_auth.controller.operator_form_controller import init_operator_form_controller
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

    def merge_config(self, config):
        ObjectHelper.copy_config_property(config, pweb_auth.common.pweb_auth_config.PWebAuthConfig)

    def init(self, pweb_app, config):
        self.merge_config(config=config)
        self.register_model()
        self.register_controller(pweb_app=pweb_app)
