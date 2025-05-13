from app.models.product import Product
from sqlalchemy.orm import Session

def create_product(db: Session):
    products = db.query(Product).all()
    for product in products:
        print(product.name, product.created_at)

    db.close()

    return {
        "success": True,
        "data": "",
        "message": "요청이 성공적으로 처리되었습니다."
    }