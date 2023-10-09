from flask import redirect, flash
from pweb_auth.common.pweb_auth_config import PWebAuthConfig
from pweb_auth.common.pweb_auth_interceptor_abc import PWebAuthBaseInterceptor
from pweb_auth.data.pweb_auth_registry import PWebAuthRegistry
from pweb_auth.security.pweb_ssr_auth import PWebSSRAuth
from pweb_form_rest.crud.pweb_request_data import RequestData
from pweb_form_rest.crud.pweb_response_maker import ResponseMaker
from pweb_form_rest.data.pweb_request_info import PWebRequestInfo


class PWebAuthInterceptor(PWebAuthBaseInterceptor):
    request_info: PWebRequestInfo = None
    request_data: RequestData = RequestData()
    response_maker: ResponseMaker = ResponseMaker()

    def get_relative_url(self):
        relative_url = self.request_info.relativeURL
        if not relative_url:
            relative_url = self.request_info.relativeURLWithParam
        return relative_url

    def is_rest_request(self) -> bool:
        relative_url = self.get_relative_url()
        if relative_url.startswith(PWebAuthConfig.REST_URL_START_WITH):
            return True
        return False

    def call_acl_interceptor(self, payload=None, pweb_ssr_auth: PWebSSRAuth = None, is_api: bool = False):
        pass

    def check_rest_auth(self):
        pass

    def check_ssr_auth(self):
        pweb_ssr_auth: PWebSSRAuth | None = PWebSSRAuth().get_auth_session()
        if not pweb_ssr_auth or not PWebSSRAuth().is_logged_in():
            flash(PWebAuthConfig.NOT_AUTHORIZE_SM, "error")
            return redirect(PWebAuthConfig.SSR_UNAUTHORIZED_REDIRECT_URL)
        return self.call_acl_interceptor(pweb_ssr_auth=pweb_ssr_auth, is_api=False)

    def check_auth(self):
        if self.is_rest_request():
            return self.check_rest_auth()
        return self.check_ssr_auth()

    def check_url_start_with(self, request_url):
        url_list = PWebAuthRegistry.SKIP_START_WITH_URL_LIST
        for url in url_list:
            if request_url.startswith(url):
                return True
        return False

    def is_url_in_skip_list(self):
        relative_url = self.get_relative_url()
        skip_url_list = PWebAuthRegistry.SKIP_URL_LIST
        if relative_url in skip_url_list or self.check_url_start_with(relative_url):
            return True
        return False

    def intercept(self):
        self.request_info = self.request_data.get_url_info()

        if self.request_info.method == 'OPTIONS':
            return self.response_maker.success_message("Allowed")

        if not self.is_url_in_skip_list():
            return self.check_auth()
