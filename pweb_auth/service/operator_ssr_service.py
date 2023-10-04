from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class OperatorSSRService:
    form_data_crud: FormDataCRUD = None

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
        return self.form_data_crud.create(view_name=view_name, form=PWebAuthConfig.OPERATOR_CREATE_DTO(), redirect_url=failed_redirect_url, params=params)

    def update(self, view_name, model_id: int, failed_redirect_url: str, update_action_url: str):
        params = {"button": "Update", "action": update_action_url, "auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.update(view_name=view_name, model_id=model_id, redirect_url=failed_redirect_url, update_form=PWebAuthConfig.OPERATOR_UPDATE_DTO(), params=params)

    def delete(self, model_id: int, redirect_url: str):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=redirect_url)

    def details(self, view_name, model_id: int, redirect_url: str):
        params = {"auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.details(view_name=view_name, model_id=model_id, redirect_url=redirect_url, params=params)

    def list(self, view_name, search_fields: list = None):
        params = {"auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.paginated_list(view_name=view_name, search_fields=search_fields, params=params)
