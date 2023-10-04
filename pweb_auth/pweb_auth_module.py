from pweb import PWebComponentRegister, PWebModuleDetails
from pweb_auth.common.pweb_auth_init import PWebAuthInit


class PWebAuthModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-auth", display_name="PWeb Auth Module")

    def run_on_cli_init(self, pweb_app, config):
        PWebAuthInit().init(pweb_app=pweb_app, config=config)

    def register_model(self, pweb_db) -> list:
        pass

    def register_controller(self, pweb_app):
        pass

    def run_on_start(self, pweb_app, config):
        PWebAuthInit().init(pweb_app=pweb_app, config=config)
