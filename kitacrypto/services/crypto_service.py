import json
import requests


from requests.adapters import HTTPAdapter

from kitacrypto.http.request import GetPriceRequest

from kitacrypto.exceptions.get_price import (
    KitaCryptoGetPriceRequestError,
    KitaCryptoGetPriceResponseError,
)


__API_URL__ = "https://api.coingecko.com/api/v3"


class CryptoService:

    api_base_url = __API_URL__

    request_timeout = 120

    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=5))

    @classmethod
    def get_price(cls, id: str, vs_currency: str) -> None:
        request = GetPriceRequest(id, vs_currency, cls.api_base_url)

        if not request.is_valid():
            raise KitaCryptoGetPriceRequestError()

        api_url = request.get_url_with_args()

        try:
            data = cls.__request(api_url)
        except Exception:
            raise KitaCryptoGetPriceResponseError()

        return data

    @classmethod
    def __request(cls, api_url: str) -> None:
        try:
            response = cls.session.get(api_url, timeout=cls.request_timeout)
        except requests.RequestException:
            raise

        try:
            response.raise_for_status()
            content = json.loads(response.content.decode("utf-8"))

            return content
        except Exception:
            try:
                content = json.loads(response.content.decode("utf-8"))
                raise ValueError(content)
            except json.JSONDecodeError:
                pass
            raise
