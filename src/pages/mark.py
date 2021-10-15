from sanic import Sanic, Request
from sanic_jinja2 import SanicJinja2
from jinja2 import FileSystemLoader
from typing import Optional
import aiohttp

app = Sanic.get_app("AsoulMark")
template = SanicJinja2(app, loader=FileSystemLoader("templates"))

@app.get("/query")
@template.template("query.html")
async def query(request: Request, param: Optional[str, int] = None):

