from app.models.product import Product
from sqlalchemy.orm import Session
from app.schemas.product import ProductQueryParams
from fastapi import Depends

def get_products(params: ProductQueryParams, db: Session):
# def get_products(db: Session):
    products = db.query(Product).all()

    total = len(products)
    db.close()

    page_data = {
        "total_items": total,
        "total_pages": total / params.perPage,
        "current_page": params.page,
        "per_page": params.perPage
    }

    return {
        "success": True,
        "data": {
            "items": products,
            "pagination": page_data
        },
        "message": "요청이 성공적으로 처리되었습니다."
    }