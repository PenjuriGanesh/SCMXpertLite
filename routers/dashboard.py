from fastapi import APIRouter,Form,HTTPException,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from  fastapi.responses import HTMLResponse,RedirectResponse

app=APIRouter()
html=Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory= "static"), name = "static")

@app.get("/dashboard")
def dashboard(request: Request):
    return html.TemplateResponse("Dashboard.py", {"request": request})