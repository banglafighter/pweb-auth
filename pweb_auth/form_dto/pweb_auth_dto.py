from marshmallow import fields, validates_schema
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.security.pweb_security_util import PWebSecurityUtil
from pweb_form_rest import PWebForm


class OperatorReadDefaultDTO(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    username = fields.Email(required=True, error_messages={"required": "Please enter username."})


class OperatorEmailBaseDefaultDTO(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})


class OperatorCreateEmailBaseDefaultDTO(OperatorEmailBaseDefaultDTO):
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class OperatorUpdateEmailBaseDefaultDTO(OperatorEmailBaseDefaultDTO):
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)


class OperatorUsernameBaseDefaultDTO(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    username = fields.Email(required=True, error_messages={"required": "Please enter username."})


class OperatorCreateUsernameBaseDefaultDTO(OperatorUsernameBaseDefaultDTO):
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class OperatorUpdateUsernameBaseDefaultDTO(OperatorUsernameBaseDefaultDTO):
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)


class LoginUsernameBaseDefaultDTO(PWebForm):
    username = fields.Email(required=True, error_messages={"required": "Please enter username."})
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
    operator = fields.Nested(PWebAuthConfig.LOGIN_RESPONSE_DTO)


class RefreshTokenResponseDefaultDTO(PWebForm):
    token = fields.Nested(LoginTokenDefaultDTO)


class ResetPasswordDefaultDTO(PWebForm):
    newPassword = fields.String(required=True, error_messages={"required": "Please enter new password."}, type="password")
    confirmPassword = fields.String(required=True, error_messages={"required": "Please enter confirm password."}, type="password")
    token = fields.String(required=True, error_messages={"required": "Please enter token."})

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
