from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

templates = Jinja2Templates(directory="templates")



villages: list[dict] = [
    {
        "name": "Cibening",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 12540,
        "area_km2": 4.3,
        "households": 3120,
        "latitude": -6.3551,
        "longitude": 107.0502
    },
    {
        "name": "Cijengkol",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 9840,
        "area_km2": 3.8,
        "households": 2410,
        "latitude": -6.3498,
        "longitude": 107.0411
    },
    {
        "name": "Cikarageman",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 11020,
        "area_km2": 4.1,
        "households": 2755,
        "latitude": -6.3447,
        "longitude": 107.0336
    },
    {
        "name": "Ciledug",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 13210,
        "area_km2": 4.7,
        "households": 3310,
        "latitude": -6.3603,
        "longitude": 107.0581
    },
    {
        "name": "Kertarahayu",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 8750,
        "area_km2": 3.5,
        "households": 2100,
        "latitude": -6.3479,
        "longitude": 107.0467
    },
    {
        "name": "Lubangbuaya",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 9650,
        "area_km2": 3.9,
        "households": 2360,
        "latitude": -6.3524,
        "longitude": 107.0375
    },
    {
        "name": "Mekarwangi",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 10420,
        "area_km2": 4.0,
        "households": 2605,
        "latitude": -6.3587,
        "longitude": 107.0294
    },
    {
        "name": "Ragemanunggal",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 11830,
        "area_km2": 4.4,
        "households": 2950,
        "latitude": -6.3415,
        "longitude": 107.0449
    },
    {
        "name": "Tamansari",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 9020,
        "area_km2": 3.6,
        "households": 2210,
        "latitude": -6.3536,
        "longitude": 107.0528
    },
    {
        "name": "Tamanrahayu",
        "district": "Setu",
        "regency": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17320",
        "population": 10860,
        "area_km2": 4.2,
        "households": 2695,
        "latitude": -6.3468,
        "longitude": 107.0397
    }
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/villages", include_in_schema=False, name="villages")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "villages": villages,
        },
    )

@app.get("/Villages/{village_name}", include_in_schema=False)
def post_page(request: Request, village_name : str):
    for village in villages:
        if village.get("name") == village_name:
            district = village["district"]
            return templates.TemplateResponse(
                "post.html",
                {
                    "request": request,
                    "village": villages,
                    "district": district,
                },
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/api/villages")
def get_posts():
    return villages


@app.get("/api/villages/{village_name}")
def get_post(village_name: str):
    for village in villages:
        if village.get("name") == village_name.capitalize():
            return village
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

# 
# @app.exception_handler(StarletteHTTPException)
# def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
#     message = (
#         exception.detail
#         if exception.detail
#         else "An error occurred. Please check your request and try again."
#     )
# 
#     if request.url.path.startswith("/api"):
#         return JSONResponse(
#             status_code=exception.status_code,
#             content={"detail": message},
#         )
# 
#     return templates.TemplateResponse(
#         "error.html",
#         {
#             "request": request,
#             "status_code": exception.status_code,
#             "title": exception.status_code,
#             "message": message,
#         },
#         status_code=exception.status_code,
#     )
# 
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