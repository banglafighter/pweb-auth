from flask import Blueprint
from pweb_auth.common.pweb_auth_config import PWebAuthConfig

operator_form_controller: Blueprint = Blueprint("operator_form_controller", __name__)


def init_operator_form_controller(url_prefix: str):
    global operator_form_controller
    operator_form_controller = Blueprint(
        "operator_form_controller",
        __name__,
        url_prefix=url_prefix,
    )
    return operator_form_controller


@operator_form_controller.route(PWebAuthConfig.LOGIN_END_POINT, methods=['POST', 'GET'])
def login():
    pass


@operator_form_controller.route(PWebAuthConfig.LOGOUT_END_POINT, methods=['GET'])
def logout():
    pass


@operator_form_controller.route(f"{PWebAuthConfig.RESET_PASS_END_POINT}/<string:token>", methods=['POST', 'GET'])
def reset_password(token: str):
    pass


@operator_form_controller.route(PWebAuthConfig.FORGOT_PASS_END_POINT, methods=['POST', 'GET'])
def forgot_password():
    pass
