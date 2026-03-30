from fastapi import Depends, FastAPI, HTTPException, Request, status, APIRouter, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.database import SessionLocal,get_db
from models.models import User
from passlib.hash import bcrypt


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "message": None
        }
    )


@router.post("/register")
def register_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    hashed_password = bcrypt.hash(password)

    new_user = User(
        username=username,
        password=hashed_password
    )

    try:
        db.add(new_user)
        db.commit()
    except IntegrityError:
        db.rollback() 
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "message": "Username sudah digunakan"
            }
        )

    return RedirectResponse("/auth/login", status_code=303)


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "message": None
        }
    )


@router.post("/login")
def login_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    


    if not user:
        db.close()
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "message": f"User dengan nama {username} tidak ditemukan"
            }
        )

    if not bcrypt.verify(password, user.password):
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "message": "Password salah"
            }
        )

    request.session["user"] = user.username
    request.session["role"] = user.role
    
    if user.role == "admin":
        return RedirectResponse("/admin", status_code=303)
    else:
        return RedirectResponse("/dashboard", status_code=303)
