class PWebAuthRegistry:
    SKIP_URL_DICT_LIST: dict[str, list[str]] = {}
    SKIP_START_WITH_URL_DICT_LIST: dict[str, list[str]] = {}

    @staticmethod
    def _init_skip_url_list(tenant: str = "default"):
        if tenant not in PWebAuthRegistry.SKIP_URL_DICT_LIST:
            PWebAuthRegistry.SKIP_URL_DICT_LIST[tenant] = []

        if tenant not in PWebAuthRegistry.SKIP_START_WITH_URL_DICT_LIST:
            PWebAuthRegistry.SKIP_START_WITH_URL_DICT_LIST[tenant] = []

    @staticmethod
    def add_url_in_skip(url: str, tenant: str = "default"):
        PWebAuthRegistry._init_skip_url_list(tenant=tenant)
        PWebAuthRegistry.SKIP_URL_DICT_LIST[tenant].append(url)

    @staticmethod
    def add_start_with_url_in_skip(url: str, tenant: str = "default"):
        PWebAuthRegistry._init_skip_url_list(tenant=tenant)
        PWebAuthRegistry.SKIP_START_WITH_URL_DICT_LIST[tenant].append(url)

    @staticmethod
    def add_url_list_in_skip(urls: list, tenant: str = "default"):
        PWebAuthRegistry._init_skip_url_list(tenant=tenant)
        if urls and isinstance(urls, list):
            PWebAuthRegistry.SKIP_URL_DICT_LIST[tenant] += urls

    @staticmethod
    def add_start_with_url_list_in_skip(urls: list, tenant: str = "default"):
        PWebAuthRegistry._init_skip_url_list(tenant=tenant)
        if urls and isinstance(urls, list):
            PWebAuthRegistry.SKIP_START_WITH_URL_DICT_LIST[tenant] += urls

    @staticmethod
    def get_skip_url_list(tenant: str = "default"):
        if tenant not in PWebAuthRegistry.SKIP_URL_DICT_LIST:
            return []
        return PWebAuthRegistry.SKIP_URL_DICT_LIST[tenant]

    @staticmethod
    def get_skip_start_with_url_list(tenant: str = "default"):
        if tenant not in PWebAuthRegistry.SKIP_START_WITH_URL_DICT_LIST:
            return []
        return PWebAuthRegistry.SKIP_START_WITH_URL_DICT_LIST[tenant]
