from jinja2 import FileSystemLoader
from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic("AsoulMark")
template = SanicJinja2(app, loader=FileSystemLoader("templates"))
app.static('/static', './statics')
from src.pages.query import query

app.add_route(query, "/query")


@app.get("/")
@template.template("query.html")
async def homepage(request):
    return None


if __name__ == '__main__':
    app.run("127.0.0.1", 8000, debug=True)
