import pweb_auth.common.pweb_auth_config
from ppy_common import ObjectHelper
from pweb_auth.model.pweb_auth_model import AuthModel


class PWebAuthInit:

    def register_model(self):
        AuthModel().init()

    def register_controller(self, pweb_app):
        pass

    def merge_config(self, config):
        ObjectHelper.copy_config_property(config, pweb_auth.common.pweb_auth_config.PWebAuthConfig)

    def init(self, pweb_app, config):
        self.merge_config(config=config)
        self.register_model()
