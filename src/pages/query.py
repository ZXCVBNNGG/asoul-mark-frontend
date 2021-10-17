from jinja2 import FileSystemLoader
from sanic import Sanic, Request
from sanic.response import redirect
from sanic_jinja2 import SanicJinja2

from ..asoul_mark.mark import get_mark, get_mark_by_uid
from ..utils.verify import is_uuid, is_uid, userUUID_get

app = Sanic.get_app("AsoulMark")
template = SanicJinja2(app, loader=FileSystemLoader("templates"))


@template.template("query.html")
async def query(request: Request):
    param = request.args.get("param")
    if is_uuid(param):
        data = await get_mark(param)
        return {"marks": [data]}
    elif is_uid(param):
        userUUID = userUUID_get(request)
        if userUUID:
            data = await get_mark_by_uid(userUUID, param)
            return {"marks": data}
        else:
            return redirect("/user")
