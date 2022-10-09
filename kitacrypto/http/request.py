from typing import Dict, Optional

from kitacrypto.helpers.parse_url import parse_url


class GetPriceRequest:
    ID = "ids"
    VS_CURRENCY = "vs_currencies"

    __slots__ = ["id", "api_url", "vs_currency"]

    def __init__(self, id, api_url: str, vs_currency: Optional[str] = "usd"):
        self.id = id
        self.vs_currency = vs_currency
        self.api_url = api_url

    def is_valid(self) -> bool:
        if self.id is not None:
            return True

        return False

    def get_params(self) -> Dict[str, str]:
        d = dict()

        d[GetPriceRequest.ID] = self.id
        d[GetPriceRequest.VS_CURRENCY] = self.VS_CURRENCY

        return d

    def get_url_with_args(self) -> str:
        params = self.get_params()
        return parse_url(self.api_url, params)
