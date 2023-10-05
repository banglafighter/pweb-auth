from pweb_form_rest.common.pweb_custom_field import BaseEnum


class AuthBase(BaseEnum):
    EMAIL = "EMAIL"
    USERNAME = "USERNAME"


class OperatorStatus(BaseEnum):
    Active = "Active"
    Inactive = "Inactive"


class OperatorAccessType(BaseEnum):
    Operator = "Operator"
    Admin = "Admin"
