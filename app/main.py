from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="templates")

# 샘플 데이터
sample_products = [
    {
        "name": "상품 A",
        "base_price": 10000,
        "currency": "KRW",
        "brand": "브랜드 A",
        "stock": 10
    },
    {
        "name": "상품 B",
        "base_price": 20000,
        "currency": "KRW",
        "brand": "브랜드 B",
        "stock": 5
    }
]

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello</h1>"

@app.get("/products", response_class=HTMLResponse)
async def get_products(request: Request):
    return templates.TemplateResponse("product_list.html", {"request": request, "products": sample_products})