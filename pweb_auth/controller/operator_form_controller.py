from flask import Blueprint

operator_form_controller: Blueprint = None


def init_operator_form_controller(url_prefix: str):
    global operator_form_controller
    operator_form_controller = Blueprint(
        "operator_form_controller",
        __name__,
        url_prefix=url_prefix,
    )
