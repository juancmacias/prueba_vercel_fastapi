from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# instalar fastapi uvicorn
# para correr el proyecto uvicorn main:app --reload
app = FastAPI()
variable_precio = 1000
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": variable_precio}
    )
