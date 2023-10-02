from flask import Blueprint
from pweb_auth.common.pweb_auth_config import PWebAuthConfig

operator_api_controller: Blueprint = Blueprint("operator_api_controller", __name__)


def init_operator_api_controller(url_prefix: str):
    global operator_api_controller
    operator_api_controller = Blueprint(
        "operator_api_controller",
        __name__,
        url_prefix=url_prefix,
    )
    return operator_api_controller


@operator_api_controller.route(PWebAuthConfig.LOGIN_END_POINT, methods=['POST'])
def login():
    pass


@operator_api_controller.route(PWebAuthConfig.LOGOUT_END_POINT, methods=['GET'])
def logout():
    pass


@operator_api_controller.route(f"{PWebAuthConfig.RESET_PASS_END_POINT}/<string:token>", methods=['GET'])
def reset_password(token: str):
    pass


@operator_api_controller.route(PWebAuthConfig.FORGOT_PASS_END_POINT, methods=['POST'])
def forgot_password():
    pass
