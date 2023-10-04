from abc import ABC, abstractmethod


class PWebAuthInterceptor(ABC):

    @abstractmethod
    def intercept_on_login(self):
        pass

    @abstractmethod
    def intercept_on_renew_token(self):
        pass

    @abstractmethod
    def intercept_on_token_generation(self):
        pass

    @abstractmethod
    def intercept_on_acl_check(self):
        pass

    @abstractmethod
    def perform_custom_login(self):
        pass
