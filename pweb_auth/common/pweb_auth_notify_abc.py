from abc import ABC, abstractmethod


class PWebAuthNotifyOnForgotPasswordRequest(ABC):
    @abstractmethod
    def perform(self):
        pass


class PWebAuthNotifyOnResetPasswordFailed(ABC):
    @abstractmethod
    def perform(self):
        pass


class PWebAuthNotifyOnResetPasswordSuccess(ABC):
    @abstractmethod
    def perform(self):
        pass


class PWebAuthNotifyOnLoginFailed(ABC):
    @abstractmethod
    def perform(self):
        pass


class PWebAuthNotifyOnLoginSuccess(ABC):
    @abstractmethod
    def perform(self):
        pass


class PWebAuthNotifyOnCreateOperator(ABC):
    @abstractmethod
    def perform(self):
        pass
