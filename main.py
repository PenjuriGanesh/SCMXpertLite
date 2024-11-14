from fastapi import FastAPI,HTTPException,Response,Request
from fastapi.templating import Jinja2Templates
from config.config import Settings
from fastapi.staticfiles import StaticFiles
from routers import signup, home, login ,forgetpassword ,dashboard
from Models.model import Signup
from fastapi.responses import HTMLResponse



app = FastAPI()
templates = Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(signup.app)
app.include_router(home.app)
app.include_router(login.app)
app.include_router(dashboard.app)
app.include_router(forgetpassword.app)
