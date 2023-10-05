from abc import ABC, abstractmethod


class PWebAuthNotifyABC(ABC):
    @abstractmethod
    def create_operator(self):
        pass

    @abstractmethod
    def login_success(self):
        pass

    @abstractmethod
    def login_failed(self):
        pass

    @abstractmethod
    def reset_password_success(self):
        pass

    @abstractmethod
    def reset_password_failed(self):
        pass

    @abstractmethod
    def forgot_password_request(self):
        pass
