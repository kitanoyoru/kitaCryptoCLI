from typing import Dict, Optional


def parse_url(
    api_url: str, params: Dict[str, str], has_params: Optional[bool] = False
) -> str:
    if params:
        api_url += "&" if has_params else "?"
        for key, value in params.items():
            if type(value) == bool:
                value = str(value).lower()
            api_url += f"{key}={value}&"
        api_url = api_url[:-1]

    return api_url
