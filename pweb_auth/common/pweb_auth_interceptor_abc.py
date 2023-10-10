from abc import ABC, abstractmethod
from typing import Tuple
from pweb_auth.model.operator_abc import OperatorAbc
from pweb_auth.security.pweb_ssr_auth import PWebSSRAuth


class PWebAuthSkipURLChecker(ABC):

    @abstractmethod
    def check(self) -> Tuple[list, list]:
        # Return skip_url_list, skip_start_with_url_list
        pass


class PWebAuthBaseInterceptor(ABC):

    @abstractmethod
    def intercept(self):
        pass


class PWebAuthInterceptOnLogin(ABC):

    @abstractmethod
    def perform(self, operator: OperatorAbc, login_data: dict):
        pass


class PWebAuthCustomLogin(ABC):

    @abstractmethod
    def perform(self, login_data: dict) -> OperatorAbc:
        pass


class PWebAuthInterceptOnACLCheck(ABC):

    @abstractmethod
    def perform(self, payload=None, pweb_ssr_auth: PWebSSRAuth = None, is_api: bool = False):
        pass


class PWebAuthInterceptOnTokenGeneration(ABC):

    @abstractmethod
    def perform(self, response: dict, operator):
        pass


class PWebAuthInterceptOnRenewToken(ABC):

    @abstractmethod
    def perform(self, token: dict, jwt_payload: dict) -> dict:
        pass
