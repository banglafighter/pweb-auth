from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class OperatorSSRService:
    form_data_crud: FormDataCRUD = FormDataCRUD(model=PWebAuthConfig.OPERATOR_MODEL)

    def login(self):
        pass

    def logout(self):
        pass

    def reset_password(self):
        pass

    def forgot_password(self):
        pass

    def create(self, view_name: str, create_action_url: str, failed_redirect_url: str):
        params = {"button": "Create", "action": create_action_url, "auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.create(view_name=view_name, form=PWebAuthConfig.OPERATOR_CREATE_DTO, redirect_url=failed_redirect_url, params=params)

    def update(self):
        pass

    def delete(self):
        pass

    def details(self):
        pass

    def list(self):
        pass
