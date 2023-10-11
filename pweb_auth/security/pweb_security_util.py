import bcrypt
from marshmallow import ValidationError


class PWebSecurityUtil:

    @staticmethod
    def get_password_hash(password, salt=None):
        if not salt:
            salt = bcrypt.gensalt()
        if password:
            password = password.encode('utf8')
        hashed = bcrypt.hashpw(password, salt)
        return hashed

    @staticmethod
    def validate_password(password, hashed):
        if password:
            password = password.encode('utf8')
        if hashed and isinstance(hashed, str):
            hashed = hashed.encode('utf8')
        if bcrypt.checkpw(password, hashed):
            return True
        return False

    @staticmethod
    def match_password(data, new_pass_key="newPassword", confirm_pass_key="confirmPassword", is_exception=True):
        if data and data[new_pass_key] == data[confirm_pass_key]:
            return True
        if not is_exception:
            return False
        raise ValidationError("New password & confirm password not matched!", "confirmPassword")
