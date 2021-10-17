from .exception import RequestError


def response_handler(response: dict):
    code = response.get("code")
    msg = response.get("msg")
    if code != 200:
        raise RequestError(code, msg)
    return response.get("data")
