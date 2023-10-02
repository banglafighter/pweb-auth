from pweb_auth.model.operator_abc import OperatorAbc
from pweb_auth.model.operator_token_abc import OperatorTokenAbc


class PWebAuthConfig:
    OPERATOR_MODEL: OperatorAbc = None
    OPERATOR_TOKEN_MODEL: OperatorTokenAbc = None
