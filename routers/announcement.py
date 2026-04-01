from fastapi import Depends, FastAPI, HTTPException, Request, status, APIRouter, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.database import SessionLocal,get_db
from models.models import User, Announcement
from passlib.hash import bcrypt


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/announcement")
def get_announ(request: Request, db: Session = Depends(get_db)):
    announcements = db.query(Announcement).all()

    return templates.TemplateResponse(
        "announcement.html",
        {
            "request": request,
            "announcements": announcements
        }
    )


@router.post("/announcement")
def post_announ(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    username = request.session.get("user")

    if not username:
        return RedirectResponse("/auth/login", status_code=303)

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_announcement = Announcement(
        title=title,
        content=content,
        author=user.username
    )

    db.add(new_announcement)
    db.commit()

    return RedirectResponse("/announcement", status_code=303)