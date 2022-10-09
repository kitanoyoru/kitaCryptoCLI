from http import HTTPStatus

from kitacrypto.exceptions.base import KitaCryptoRequestError


class KitaCryptoGetPriceRequestError(KitaCryptoRequestError):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(HTTPStatus.BAD_REQUEST, "check the entered data")


class KitaCryptoGetPriceResponseError(Exception):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(123, "temp")
