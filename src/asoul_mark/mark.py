from ..utils.handler import response_handler
from ..utils.requests import get

api = "https://api.asoul-mark.xyz"


async def get_mark(markUUID):
    resp = await get(api + "/mark/get", params={"markUUID": markUUID})
    return response_handler(resp)


async def get_mark_by_uid(userUUID, uid):
    header = {"UserUUID": userUUID}
    resp = await get(api + "/mark/get_by_uid", params={"uid": uid}, headers=header)
    return response_handler(resp)
