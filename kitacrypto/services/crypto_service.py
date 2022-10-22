import json
import requests

from typing import Optional

from requests.adapters import HTTPAdapter

from kitacrypto.config.config import __API_URL__
from kitacrypto.http.request import GetPriceRequest
from kitacrypto.exceptions.get_price import (
    KitaCryptoGetPriceRequestError,
    KitaCryptoGetPriceResponseError,
)



class CryptoService:
    api_base_url = __API_URL__

    request_timeout = 120

    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=5))

    @classmethod
    def get_price(cls, id: str, vs_currency: Optional[str] = "usd") -> Optional[str]:
        request = GetPriceRequest(id, cls.api_base_url, vs_currency, )

        if not request.is_valid():
            raise KitaCryptoGetPriceRequestError(123, "temp") # FIX: Handle exception

        api_url = request.get_url_with_args()

        try:
            data = cls.__request(api_url)
        except Exception:
            raise KitaCryptoGetPriceResponseError(123, "temp") # FIX: Handle exception

        return data

    @classmethod
    def __request(cls, api_url: str) -> Optional[str]:
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
