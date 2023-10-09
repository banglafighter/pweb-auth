class PWebAuthRegistry:
    SKIP_URL_LIST: list[str] = []
    SKIP_START_WITH_URL_LIST: list[str] = []

    @staticmethod
    def add_url_in_skip(url: str):
        PWebAuthRegistry.SKIP_URL_LIST.append(url)

    @staticmethod
    def add_start_with_url_in_skip(url: str):
        PWebAuthRegistry.SKIP_START_WITH_URL_LIST.append(url)

    @staticmethod
    def add_url_list_in_skip(urls: list):
        if urls and isinstance(urls, list):
            PWebAuthRegistry.SKIP_URL_LIST += urls

    @staticmethod
    def add_start_with_url_list_in_skip(urls: list):
        if urls and isinstance(urls, list):
            PWebAuthRegistry.SKIP_START_WITH_URL_LIST += urls
