from flask import redirect

from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.form_dto.pweb_auth_dto import ResetPasswordDefaultDTO
from pweb_auth.service.operator_service import OperatorService
from pweb_form_rest import PWebForm
from pweb_auth.data.pweb_auth_enum import AuthBase
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class OperatorSSRService:
    form_data_crud: FormDataCRUD = None
    operator_service = OperatorService()

    def login(self, view_name, success_redirect_url: str):
        form = PWebAuthConfig.LOGIN_DTO()
        params = {"auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.render(view_name=view_name, params=params, form=form)

    def logout(self, logout_redirect_url: str):
        return redirect(logout_redirect_url)

    def reset_password(self, view_name, reset_response_view, token: str):
        form = ResetPasswordDefaultDTO()
        params = {"token": token}
        return self.form_data_crud.render(view_name=view_name, params=params, form=form)

    def forgot_password(self, view_name, forgot_response_view):
        form = PWebAuthConfig.FORGOT_PASSWORD_DTO()
        params = {"auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.render(view_name=view_name, params=params, form=form)

    def _check_unique(self, form: PWebForm, model_id: int = None):
        if form.is_post_data() and form.is_valid_data():
            data = form.get_request_data()
            is_broken_integrity = self.operator_service.is_operator_integrity_broken(request_data=data, model_id=model_id)
            auth_base = PWebAuthConfig.SYSTEM_AUTH_BASE
            error_message = "Already used"
            if is_broken_integrity and auth_base == AuthBase.EMAIL:
                form.set_field_error("email", error_message)
            elif is_broken_integrity and auth_base == AuthBase.USERNAME:
                form.set_field_error("username", error_message)

    def create(self, view_name: str, create_action_url: str, failed_redirect_url: str):
        params = {"button": "Create", "action": create_action_url, "auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        form = PWebAuthConfig.OPERATOR_CREATE_DTO()
        self._check_unique(form=form)
        return self.form_data_crud.create(view_name=view_name, form=form, redirect_url=failed_redirect_url, params=params)

    def update(self, view_name, model_id: int, failed_redirect_url: str, update_action_url: str):
        params = {"button": "Update", "action": update_action_url, "auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        update_form = PWebAuthConfig.OPERATOR_UPDATE_DTO()
        self._check_unique(form=update_form, model_id=model_id)
        return self.form_data_crud.update(view_name=view_name, model_id=model_id, redirect_url=failed_redirect_url, update_form=update_form, params=params)

    def delete(self, model_id: int, redirect_url: str):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=redirect_url)

    def details(self, view_name, model_id: int, redirect_url: str):
        params = {"auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.details(view_name=view_name, model_id=model_id, redirect_url=redirect_url, params=params)

    def list(self, view_name, search_fields: list = None):
        params = {"auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name}
        return self.form_data_crud.paginated_list(view_name=view_name, search_fields=search_fields, params=params)
