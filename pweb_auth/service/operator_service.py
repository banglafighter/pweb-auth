from ppy_common import DataUtil
from pweb_auth.model.pweb_auth_model import AuthModel
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.data.pweb_auth_enum import AuthBase


class OperatorService:

    def is_username_available(self, username: str, model_id: int = None):
        operator = AuthModel.operator.query.filter(AuthModel.operator.username == username).first()
        if operator:
            if model_id and operator.id == model_id:
                return True
            return False
        return True

    def is_email_available(self, email: str, model_id: int = None):
        operator = AuthModel.operator.query.filter(AuthModel.operator.email == email).first()
        if operator:
            if model_id and operator.id == model_id:
                return True
            return False
        return True

    def is_operator_integrity_broken(self, request_data: dict, model_id: int):
        auth_base = PWebAuthConfig.SYSTEM_AUTH_BASE
        is_broken_integrity = True
        if auth_base == AuthBase.EMAIL:
            email = DataUtil.get_dict_value(request_data, "email")
            is_broken_integrity = not self.is_email_available(email=email, model_id=model_id)
        elif auth_base == AuthBase.USERNAME:
            username = DataUtil.get_dict_value(request_data, "username")
            is_broken_integrity = not self.is_username_available(username=username, model_id=model_id)
        return is_broken_integrity
