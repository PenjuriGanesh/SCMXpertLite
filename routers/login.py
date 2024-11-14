from fastapi import APIRouter, FastAPI, Request, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import Settings
from Models.model import Signup

app = APIRouter()
html = Jinja2Templates(directory="Templates")
collection2 = Settings.collection2
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/login")
def login(request: Request):
    return html.TemplateResponse("Login.html", {"request": request})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        # Find the user in the database by username
        user_data = collection2.find_one({"user": username})

        if user_data:
            if password == user_data["password"]:
                # Successfully logged in, return user info (redirect to dashboard)
                response_content = {
                    "message": "Login successful",
                    "username": user_data["user"],
                    "email": user_data["email"],
                    "role": user_data["role"]
                }
                # Redirect the user to the dashboard page
                return RedirectResponse(url="/dashboard.py", status_code=303)

            else:
                raise HTTPException(status_code=401, detail="Password is incorrect")
        else:
            raise HTTPException(status_code=401, detail="Username not found")

    except HTTPException as http_exception:
        # Handle HTTPException (validation errors) separately
        return JSONResponse(content={"detail": http_exception.detail}, status_code=http_exception.status_code)
    except Exception as e:
        # Handle other exceptions with a 500 status code
        return JSONResponse(content={"detail": str(e)}, status_code=500)
