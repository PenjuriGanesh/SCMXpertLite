from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import logging
from config.config import Settings
from Models.model import Signup
from fastapi.staticfiles import StaticFiles
import re  # For regex validation

app = APIRouter()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize collection and template renderer
collection2 = Settings.collection2
html = Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/signup", response_class=HTMLResponse)
def sign(request: Request):
    # Render the signup page with no error message initially
    return html.TemplateResponse("sign_up.html", {"request": request, "error_message": None})

@app.post("/signup", response_class=HTMLResponse)
def sign(request: Request, username: str = Form(...), email: str = Form(...), role: str = Form("user"),
         password: str = Form(...), confirm: str = Form(...)):
    try:
        # Check for existing user or email
        existing_user = collection2.find_one({"user": username})  
        existing_email = collection2.find_one({"email": email})

        # Validation checks and corresponding error messages
        if existing_user:
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Username already used"})
        
        if existing_email:
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Email already used"})

        if password != confirm:
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Passwords do not match"})

        if not password[0].isupper():
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Password should start with a capital letter"})

        if len(password) < 7:
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Password should be at least 7 characters long"})

        if not any(char.isdigit() for char in password):
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Password should contain at least one digit"})

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return html.TemplateResponse("sign_up.html", {"request": request, "error_message": "Password should contain at least one special character"})

        # Create the Signup object and insert it into the collection
        signup1 = Signup(user=username, email=email, role=role, password=password, confirmpassword=confirm)
        collection2.insert_one(dict(signup1)) 

        # Log success
        logging.info(f"User {username} successfully signed up")

        return RedirectResponse(url='/login', status_code=303)

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")  # Log any unexpected error
        return html.TemplateResponse("sign_up.html", {"request": request, "error_message": f"Internal Server Error: {str(e)}"})
