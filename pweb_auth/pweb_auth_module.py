from pweb import PWebComponentRegister
from pweb_auth.common.pweb_auth_init import PWebAuthInit


class PWebAuthModule(PWebComponentRegister):

    def run_on_cli_init(self, pweb_app, config):
        pass

    def register_model(self, pweb_db) -> list:
        pass

    def register_controller(self, pweb_app):
        pass

    def run_on_start(self, pweb_app, config):
        PWebAuthInit().init(pweb_app=pweb_app, config=config)
