from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse,HTMLResponse
from fastapi.templating import Jinja2Templates
from db.database import SessionLocal,get_db
from sqlalchemy.orm import Session
from models.models import User, Announcement, Report

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    username = request.session.get("user")
    if request.session.get("role") != "user":
        return RedirectResponse("/dashboard-admin", status_code=303)


    return templates.TemplateResponse(
        "dashboard_user.html",
        {
            "request": request,
            "username": username
        }
    )


@router.get("/dashboard-admin")
def admin_dashboard(request: Request, db: Session = Depends(get_db)):

    if not request.session.get("user"):
        return RedirectResponse("/auth/login", status_code=303)


    latest_announcements = db.query(Announcement).order_by(Announcement.id.desc()).limit(2).all()
  
    total_reports = db.query(Report).count()

    latest_reports = db.query(Report).order_by(Report.id.desc()).limit(2).all()

    approved_reports = db.query(Report).filter(Report.status == "approved").count()

    rejected_reports = db.query(Report).filter(Report.status == "rejected").count()

    processed_reports = db.query(Report).filter(Report.status == "process").count()

    pending_reports = db.query(Report).filter(Report.status == "pending").count()



    if request.session.get("role") != "admin":
        return RedirectResponse("/dashboard", status_code=303)

    return templates.TemplateResponse(
        "dashboard_admin.html",
        {
            "request": request,
            "username": request.session.get("user"),
            "total_reports": total_reports,
            "approved_reports": approved_reports,
            "rejected_reports": rejected_reports,
            "processed_reports": processed_reports,
            "pending_reports": pending_reports,
            "latest_announcements": latest_announcements,
            "latest_reports": latest_reports
            
        }
    )