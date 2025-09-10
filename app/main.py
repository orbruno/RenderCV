from fastapi import FastAPI, Request
from fastapi.responses import Response, HTMLResponse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import os

import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("weasyprint").setLevel(logging.DEBUG)

from urllib.parse import urlparse
from fastapi.templating import Jinja2Templates


def base_url(url):
    parsed = urlparse(url)
    # If scheme is missing, just use netloc + path
    if parsed.scheme:
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    return (
        f"{parsed.netloc}{parsed.path}" if parsed.netloc else parsed.path.split("?")[0]
    )


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
jinja_env.filters["base_url"] = base_url

templates = Jinja2Templates(directory="app/templates")
templates.env.filters["base_url"] = base_url

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/render-cv")
async def render_cv(request: Request):
    data = await request.json()
    template = jinja_env.get_template("cv.html")
    html_content = template.render(**data)
    base_url = os.path.abspath(os.path.dirname(__file__))
    css_path = os.path.join(os.path.dirname(__file__), "templates", "cv.css")
    pdf = HTML(string=html_content, base_url=base_url).write_pdf(
        stylesheets=[CSS(css_path)]
    )
    return Response(content=pdf, media_type="application/pdf")
