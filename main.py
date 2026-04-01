from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Request, status, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException as StarletteHTTPExceptison
from routers import auth, dashboard, announcement
from db.database import Base, engine
from starlette.middleware.sessions import SessionMiddleware



app = FastAPI()

Base.metadata.create_all(bind=engine)

router = APIRouter()

app.add_middleware(SessionMiddleware, secret_key="secret123")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth.router, prefix="/auth")
app.include_router(dashboard.router)
app.include_router(announcement.router)

templates = Jinja2Templates(directory="templates")

@app.get("/html")
def html_page(request: Request):
    return templates.TemplateResponse("test.html", {
        "request": request,
        "name": "Naufal"
    })

