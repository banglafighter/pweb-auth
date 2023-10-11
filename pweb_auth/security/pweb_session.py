from flask import session


class PWebSession:
    autoPrefix = "pweb_auth_"

    @staticmethod
    def add(key: str, value):
        session[PWebSession.autoPrefix + key] = value

    @staticmethod
    def get(key: str, default=None):
        store_key = PWebSession.autoPrefix + key
        if store_key in session:
            return session[store_key]
        return default

    @staticmethod
    def remove(key: str):
        store_key = PWebSession.autoPrefix + key
        if store_key in session:
            del session[store_key]

    @staticmethod
    def destroy():
        session.clear()

    @staticmethod
    def all(default=None):
        key_values = {}
        for item in session:
            key = str(item)
            if key and key.startswith(PWebSession.autoPrefix):
                key_values[key[len(PWebSession.autoPrefix):]] = session[key]
        if key_values:
            return key_values
        return default
