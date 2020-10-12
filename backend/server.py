from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import loguru
logger = loguru.logger
app = FastAPI()

@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    logger.debug('id: {}',id)
    return templates.TemplateResponse("test.html", {"request": request, "id": id})


app.mount("/", StaticFiles(directory="dist"), name="dist")

# 创建一个templates（模板）对象，以后可以重用。
templates = Jinja2Templates(directory="dist")

# Request在路径操作中声明一个参数，该参数将返回模板。
# 使用templates您创建的渲染并返回TemplateResponse，并request在Jinja2“上下文” 中将用作键值对之一。

