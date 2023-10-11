from pweb_auth.security.pweb_security_util import PWebSecurityUtil
from pweb_orm import pweb_orm, PwebModel


class OperatorAbc(PwebModel):
    __abstract__ = True
    firstName = pweb_orm.Column("first_name", pweb_orm.String(100))
    lastName = pweb_orm.Column("last_name", pweb_orm.String(100))
    name = pweb_orm.Column("name", pweb_orm.String(100))
    email = pweb_orm.Column("email", pweb_orm.String(100), unique=True, index=True)
    username = pweb_orm.Column("username", pweb_orm.String(100), unique=True, index=True)
    password_hash = pweb_orm.Column("password_hash", pweb_orm.String(150), nullable=False, index=True)
    isVerified = pweb_orm.Column("is_verified", pweb_orm.Boolean, default=True)
    status = pweb_orm.Column("status", pweb_orm.String(25), default="Active")
    accessType = pweb_orm.Column("access_type", pweb_orm.String(25), default="Operator")
    token = pweb_orm.Column("token", pweb_orm.String(200))
    profilePhoto = pweb_orm.Column("profile_photo", pweb_orm.String(200))
    coverPhoto = pweb_orm.Column("cover_photo", pweb_orm.String(200))

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = PWebSecurityUtil.get_password_hash(password)

    def verify_password(self, password) -> bool:
        return PWebSecurityUtil.validate_password(password, self.password_hash)
