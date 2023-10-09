from abc import ABC, abstractmethod
from pweb_auth.model.operator_abc import OperatorAbc


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
    def perform(self):
        pass


class PWebAuthInterceptOnTokenGeneration(ABC):

    @abstractmethod
    def perform(self):
        pass


class PWebAuthInterceptOnRenewToken(ABC):

    @abstractmethod
    def perform(self):
        pass
