from flask import Blueprint

operator_api_controller: Blueprint = None


def init_operator_api_controller(url_prefix: str):
    global operator_api_controller
    operator_api_controller = Blueprint(
        "operator_api_controller",
        __name__,
        url_prefix=url_prefix,
    )
