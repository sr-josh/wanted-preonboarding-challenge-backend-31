from fastapi import APIRouter

router = APIRouter()

@router.post("")
def create_products():
    return {"message": "product registered"}

@router.get("")
def get_products():
    return {"message": "product list"}

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

