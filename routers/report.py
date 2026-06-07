from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, Request, status, APIRouter, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import desc, case, or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.database import SessionLocal,get_db
from models.models import User, Announcement, Report


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/report")
def get_report(request: Request, db: Session = Depends(get_db)):
  
      username = request.session.get("user")
      role = request.session.get("role")


  
      if not username:
          return RedirectResponse("/auth/login", status_code=303)
      if role == "admin":
          return RedirectResponse("/admin/report")
  
      reports = db.query(Report).filter(
          Report.username == username
      ).all()
  
      return templates.TemplateResponse(
          "report.html",
          {
              "request": request,
              "reports": reports,
              "role": request.session.get("role")
          }
      )
  
@router.post("/report")
def post_report(request: Request,
    type: str = Form(...),
    description: str = Form(...),
    location: str = Form(...),
    db: Session = Depends(get_db)
):
    username = request.session.get("user")
    role = request.session.get("role")
    
    if not username:
        return RedirectResponse("/auth/login", status_code=303)
    
    if role == "admin":
        return RedirectResponse("/report", status_code=303)

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")


    new_report = Report(
        type = type,
        description = description,
        location = location,
        status = "pending",
        username = user.username
    )

    db.add(new_report)
    db.commit()

    return RedirectResponse(f"/report?success=report_created&id={new_report.id}", status_code=303
    )



@router.get("/report/laporan-saya")
def my_report(request:Request,  db: Session = Depends(get_db)):
    username = request.session.get("user")
    role = request.session.get("role")



    report = db.query(Report).filter(Report.username == username).order_by(Report.id.desc()).all()
<<<<<<< HEAD

=======
>>>>>>> v2
  
    if not username:
      return RedirectResponse("/auth/login", status_code=303)

      
    return templates.TemplateResponse(
        "my_report.html",
        {
            "request": request,
            "reports": report,
            "role": role
        }
    )


@router.post("/report/delete/{report_id}")
def delete_report(
    report_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    username = request.session.get("user")
    role = request.session.get("role")

    if not username:
        return RedirectResponse("/auth/login", status_code=303)

    report = db.query(Report).filter(Report.id == report_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    #==========================================
    if role != "admin" and report.username != username:
        raise HTTPException(status_code=403, detail="Not allowed")

    #   #==========================================
    if role != "admin" and report.status != "pending":
        raise HTTPException(status_code=403, detail="Cannot delete this report")

    db.delete(report)
    db.commit()

    return RedirectResponse("/report", status_code=303)




#================== ADMIN SECTION ===================


@router.get("/admin/report")
def get_report_admin(request: Request, db: Session = Depends(get_db)):
  
      username = request.session.get("user")
      role = request.session.get("role")
    
      if not username:
        return RedirectResponse("/auth/login", status_code=303)
    
      if role != "admin":
        return RedirectResponse("/report", status_code=303)

  
      reports = db.query(Report).order_by(Report.id.desc()).all()
      
      
      return templates.TemplateResponse(
          "report_admin.html",
          {
              "request": request,
              "reports": reports,
              "role": role
          }
      )


@router.get("/report/{report_id}/inspect")
def inspect_report(request:Request, report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    username = request.session.get("user")
    role = request.session.get("role")

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
  
    if not username:
      return RedirectResponse("/auth/login", status_code=303)

    if role == "user" and report.username != username:
      raise HTTPException(status_code=403, detail="Forbidden")

      
    return templates.TemplateResponse(
        "inspect.html",
        {
            "request": request,
            "report": report,
            "role": role
        }
    )


@router.post("/report/{report_id}/approve")
def approve_report(request:Request, report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    username = request.session.get("user")
    role = request.session.get("role")

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
  
    if not username:
      return RedirectResponse("/auth/login", status_code=303)
  
    if role != "admin":
      return RedirectResponse("/report", status_code=303)


    report.status = "approved"
    db.commit()

    return RedirectResponse("/admin/report", status_code=303)


@router.post("/report/{report_id}/reject")
def reject_report(request:Request, report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    username = request.session.get("user")
    role = request.session.get("role")

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
  
    if not username:
      return RedirectResponse("/auth/login", status_code=303)
  
    if role != "admin":
      return RedirectResponse("/report", status_code=303)


    report.status = "rejected"
    db.commit()

    return RedirectResponse("/admin/report", status_code=303)



@router.post("/report/{report_id}/process")
def process_report(request:Request, report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    username = request.session.get("user")
    role = request.session.get("role")

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
  
    if not username:
      return RedirectResponse("/auth/login", status_code=303)
  
    if role != "admin":
      return RedirectResponse("/report", status_code=303)


    report.status = "process"
    db.commit()

    return RedirectResponse("/admin/report", status_code=303)
