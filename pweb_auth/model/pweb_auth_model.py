from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.model.operator_abc import OperatorAbc
from pweb_auth.model.operator_token_abc import OperatorTokenAbc


class AuthModel:
    operator: OperatorAbc = None
    operatorToken: OperatorTokenAbc = None

    def init(self):
        self.init_operator()
        self.init_operator_token()

    def init_operator(self):
        if PWebAuthConfig.OPERATOR_MODEL:
            AuthModel.operator = PWebAuthConfig.OPERATOR_MODEL
        else:
            class Operator(OperatorAbc):
                pass

            PWebAuthConfig.OPERATOR_MODEL = AuthModel.operator = Operator

    def init_operator_token(self):
        if PWebAuthConfig.OPERATOR_TOKEN_MODEL:
            AuthModel.operatorToken = PWebAuthConfig.OPERATOR_TOKEN_MODEL
        else:
            class OperatorToken(OperatorTokenAbc):
                pass

            PWebAuthConfig.OPERATOR_TOKEN_MODEL = AuthModel.operatorToken = OperatorToken
