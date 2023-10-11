from sqlalchemy import Integer
from pweb_orm import PWebRelationalModel, pweb_orm


class OperatorTokenAbc(PWebRelationalModel):
    __abstract__ = True
    token = pweb_orm.Column("token", pweb_orm.String(350), nullable=False)
    name = pweb_orm.Column("name", pweb_orm.String(25))
    tokenOwnerId = pweb_orm.Column("token_owner_id", pweb_orm.BigInteger().with_variant(Integer, "sqlite"), nullable=False)
