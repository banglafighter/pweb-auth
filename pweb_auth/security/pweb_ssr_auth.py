from ppy_common import DataUtil
from ppy_jsonyml import ODConverter
from ppy_jsonyml.converter.od_base import ODBase
from pweb_auth.security.pweb_session import PWebSession


class PWebSSRAuthData(ODBase):
    isLoggedIn: bool = False
    firstName: str = None
    lastName: str = None
    name: str = None
    email: str = None
    username: str = None
    id: int = None
    uuid: str = None
    profilePhoto: str = None
    coverPhoto: str = None


class PWebSSRAuth:
    od_converter = ODConverter()
    _AUTH_SESSION_KEY = "AUTH_DETAILS"

    def add_data_to_session(self, operator, auth_data: PWebSSRAuthData):
        auth_data = DataUtil.copy_object_to_object(source_object=operator, dst_object=auth_data)
        auth_data_dict = self.od_converter.get_dict(od_object=auth_data)
        if auth_data_dict and auth_data.isLoggedIn:
            PWebSession.add(self._AUTH_SESSION_KEY, auth_data_dict)
            return True
        return False

    def perform_login_process(self, operator):
        if not operator and not hasattr(operator, "id"):
            return False
        auth = PWebSSRAuthData()
        auth.isLoggedIn = True
        return self.add_data_to_session(operator=operator, auth_data=auth)

    def logout(self):
        PWebSession.destroy()

    def is_logged_in(self):
        auth_data: PWebSSRAuthData = self.get_auth_session()
        if auth_data and auth_data.isLoggedIn:
            return auth_data.isLoggedIn
        return False

    def get_auth_session(self) -> PWebSSRAuthData | None:
        session_auth_data = PWebSession.get(self._AUTH_SESSION_KEY)
        if not session_auth_data or not isinstance(session_auth_data, dict):
            return None
        auth_data: PWebSSRAuthData = self.od_converter.get_object(data=session_auth_data, od_object=PWebSSRAuthData())
        return auth_data
