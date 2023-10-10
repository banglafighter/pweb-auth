from marshmallow import fields, validates_schema
from pweb_auth.data.pweb_auth_enum import OperatorStatus, OperatorAccessType
from pweb_auth.security.pweb_security_util import PWebSecurityUtil
from pweb_form_rest import PWebForm, EnumField
from pweb_orm import PWebORMUtil


class OperatorReadDefaultDTO(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    username = fields.String(required=True, error_messages={"required": "Please enter username."})
    status = EnumField(OperatorStatus, required=True, error_messages={"required": "Please select status"}, placeholder="Select status", defaultValue="Active")
    accessType = EnumField(OperatorAccessType, required=True, error_messages={"required": "Please select access"}, placeholder="Select access type")


class OperatorBaseDefaultDTO(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    status = EnumField(OperatorStatus, required=True, error_messages={"required": "Please select status"}, placeholder="Select status", defaultValue="Active")
    accessType = EnumField(OperatorAccessType, required=True, error_messages={"required": "Please select access"}, placeholder="Select access type")

    @validates_schema
    def validates_schema(self, data, **kwargs):
        PWebORMUtil.enum_to_string(data, "status")
        PWebORMUtil.enum_to_string(data, "accessType")


class OperatorEmailBaseDefaultDTO(OperatorBaseDefaultDTO):
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})


class OperatorCreateEmailBaseDefaultDTO(OperatorEmailBaseDefaultDTO):
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class OperatorUpdateEmailBaseDefaultDTO(OperatorEmailBaseDefaultDTO):
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)


class OperatorUsernameBaseDefaultDTO(OperatorBaseDefaultDTO):
    username = fields.String(required=True, error_messages={"required": "Please enter username."})


class OperatorCreateUsernameBaseDefaultDTO(OperatorUsernameBaseDefaultDTO):
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class OperatorUpdateUsernameBaseDefaultDTO(OperatorUsernameBaseDefaultDTO):
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)


class LoginUsernameBaseDefaultDTO(PWebForm):
    username = fields.String(required=True, error_messages={"required": "Please enter username."})
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class LoginEmailBaseDefaultDTO(PWebForm):
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class LoginTokenDefaultDTO(PWebForm):
    accessToken = fields.String(dump_only=True)
    refreshToken = fields.String(dump_only=True)


class RefreshTokenDefaultDTO(PWebForm):
    refreshToken = fields.String(required=True, error_messages={"required": "Please enter refresh token."})


class LoginResponseDefaultDTO(PWebForm):
    token = fields.Nested(LoginTokenDefaultDTO)
    operator = fields.Nested(OperatorReadDefaultDTO())


class RefreshTokenResponseDefaultDTO(PWebForm):
    token = fields.Nested(LoginTokenDefaultDTO)


class ResetPasswordDefaultDTO(PWebForm):
    newPassword = fields.String(required=True, error_messages={"required": "Please enter new password."}, type="password")
    confirmPassword = fields.String(required=True, error_messages={"required": "Please enter confirm password."}, type="password")
    token = fields.String(required=True, error_messages={"required": "Please enter token."}, type="hidden", isLabel=False)

    @validates_schema
    def validate_schema(self, data, **kwargs):
        PWebSecurityUtil.match_password(data=data)


class ChangePasswordDefaultDTO(ResetPasswordDefaultDTO):
    oldPassword = fields.String(required=True, error_messages={"required": "Please enter old password."}, type="password")
    newPassword = fields.String(required=True, error_messages={"required": "Please enter new password."}, type="password")
    confirmPassword = fields.String(required=True, error_messages={"required": "Please enter confirm password."}, type="password")

    @validates_schema
    def validate_schema(self, data, **kwargs):
        PWebSecurityUtil.match_password(data=data)


class AdminResetPasswordDefaultDTO(ResetPasswordDefaultDTO):
    newPassword = fields.String(required=True, error_messages={"required": "Please enter new password."}, type="password")
    confirmPassword = fields.String(required=True, error_messages={"required": "Please enter confirm password."}, type="password")

    @validates_schema
    def validate_schema(self, data, **kwargs):
        PWebSecurityUtil.match_password(data=data)


class ForgotPasswordEmailBaseDefaultDTO(PWebForm):
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})


class ForgotPasswordUsernameBaseDefaultDTO(PWebForm):
    username = fields.Email(required=True, error_messages={"required": "Please enter username."})
