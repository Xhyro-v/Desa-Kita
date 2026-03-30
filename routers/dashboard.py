from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse,HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    username = request.session.get("user")

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "username": username
        }
    )


@router.get("/admin")
def admin_dashboard(request: Request):
    if not request.session.get("user"):
        return RedirectResponse("/auth/login", status_code=303)

    if request.session.get("role") != "admin":
        return RedirectResponse("/dashboard", status_code=303)

    return templates.TemplateResponse(
      "admin.html",
      {
        "request": request,
        "username": request.session.get("user")
    }
  )