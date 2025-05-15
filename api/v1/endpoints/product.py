from fastapi import APIRouter, Depends
from app.commands.product.create_product import create_product
from app.queries.product.get_product import get_products
from app.database import get_session
from app.schemas.product import ProductQueryParams
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("")
def create():
    return create_product()

@router.get("")
def get_product(params: ProductQueryParams = Depends(), db: Session = Depends(get_session)):
# def get_product(db: Session = Depends(get_session)):
    return get_products(params, db)
    # return get_products(db)

@router.get("/{id}")
def get_product(id: int):
    return {"message": "product ready", "id": id}

@router.put("/{id}")
def update_product(id: int):
    return {"message": "product updated", "id": id}

@router.delete("/{id}")
def delete_products(id: int):
    return {"message": "product deleted", "id": id}

@router.post("/{id}/options")
def add_options(id: int):
    return {"message": "option added", "id": id}

@router.put("/{id}/options/{optionId}")
def update_options(id: int, optionId: int):
    return {"message": "option updated", "id": id, "optionId": optionId}


@router.delete("/{id}/options/{optionId}")
def delete_options(id: int):
    return {"message": "option deleted", "id": id}

@router.post("/{id}/images")
def add_images(id: int):
    return {"message": "image added", "id": id}

