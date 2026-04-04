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
            "announcements": announcements,
            "role" : request.session.get("role"),
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
    role = request.session.get("role")

    if not username:
        return RedirectResponse("/auth/login", status_code=303)
    
    if role != "admin":
        return RedirectResponse("/announcement",status_code=303)

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


@router.post("/announcement/delete/{ann.id}")
def delete_announ(
    ann_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    role = request.session.get("role")

    if role != "admin":
        return RedirectResponse("/announcement", status_code=303)

    announcement = db.query(Announcement).filter(Announcement.id == ann_id).first()

    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    db.delete(announcement)
    db.commit()

    return RedirectResponse("/announcement", status_code=303)