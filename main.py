from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

announcements: list[dict] = [
    {
        "id": 1,
        "title": "Kerja Bakti Mingguan",
        "content": "Seluruh warga Desa Cibening diharapkan mengikuti kegiatan kerja bakti pada hari Minggu pukul 07.00 WIB di area balai desa dan jalan utama.",
        "date": "2026-03-16",
        "author": "Admin Desa"
    },
    {
        "id": 2,
        "title": "Jadwal Posyandu Bulan Maret",
        "content": "Posyandu Melati akan dilaksanakan pada tanggal 20 Maret 2026 pukul 09.00 WIB di Gedung Serbaguna Desa.",
        "date": "2026-03-15",
        "author": "Kader Posyandu"
    },
    {
        "id": 3,
        "title": "Pendaftaran Turnamen Futsal Antar RT",
        "content": "Dalam rangka memperingati Hari Jadi Desa, akan diadakan turnamen futsal antar RT. Pendaftaran dibuka sampai tanggal 25 Maret 2026.",
        "date": "2026-03-14",
        "author": "Karang Taruna"
    },
    {
        "id": 4,
        "title": "Perbaikan Jalan Desa",
        "content": "Mulai tanggal 18 Maret 2026 akan dilakukan perbaikan jalan di wilayah RT 03. Warga diharapkan berhati-hati saat melintas.",
        "date": "2026-03-13",
        "author": "Pemerintah Desa"
    },
    {
        "id": 5,
        "title": "Pengajian Rutin Jumat Malam",
        "content": "Pengajian rutin warga akan dilaksanakan setiap Jumat malam setelah sholat Isya di Masjid Al-Ikhlas.",
        "date": "2026-03-12",
        "author": "DKM Masjid"
    }
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/announcements", include_in_schema=False, name="announcements")
@app.get("/news", include_in_schema=False, name="news")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "announcements": announcements,
        },
    )

@app.get("/announcements/{announcements_id}", include_in_schema=False)
def post_page(request: Request, announcements_id : int):
    for announcement in announcements:
        if announcement.get("id") == announcements_id :
            return templates.TemplateResponse(
                  "announcements.html",
                  {
                      "request": request,
                      "announcement" : announcement,
                  },
              
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/news/{news_id}", include_in_schema=False)
def post_page(request: Request, news_id : int):
    for nw in news:
        if nw.get("id") == news_id :
            return templates.TemplateResponse(
                  "news.html",
                  {
                      "request": request,
                      "nw" : nw,
                  },
              
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")



@app.get("/api/announcements")
def get_posts():
    return announcements


@app.get("/api/announcements/{announcements_id}")
def get_post(announcements_id: int):
    for announcement in announcements:
        if announcement.get("id") == announcements_id :
            return announcement
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")





# cari village yang name == village_name
# kalau ketemu:
#    render post.html
# kalau nggak ketemu:
#    raise 404






# 
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )

    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )






# 
# @app.exception_handler(RequestValidationError)
# def validation_exception_handler(request: Request, exception: RequestValidationError):
#     if request.url.path.startswith("/api"):
#         return JSONResponse(
#             status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#             content={"detail": exception.errors()},
#         )
# 
#     return templates.TemplateResponse(
#         "error.html",
#         {
#            "request": request,
#            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
#             "title": status.HTTP_422_UNPROCESSABLE_ENTITY,
#             "message": "Invalid request. Please check your input and try again.",
#         },
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#     )