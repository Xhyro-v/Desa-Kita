import uvicorn, os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Request, status, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException as StarletteHTTPExceptison
from routers import auth, dashboard, announcement, report
from db.database import Base, engine
from starlette.middleware.sessions import SessionMiddleware

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

Base.metadata.create_all(bind=engine)

router = APIRouter()

app.add_middleware(SessionMiddleware,secret_key=SECRET_KEY)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth.router, prefix="/auth")
app.include_router(dashboard.router)
app.include_router(announcement.router)
app.include_router(report.router)

templates = Jinja2Templates(directory="templates")




if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )