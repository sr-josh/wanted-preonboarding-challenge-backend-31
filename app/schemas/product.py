from typing import List, Optional
from pydantic import BaseModel

class ProductQueryParams(BaseModel):
    page: Optional[int] = 1
    perPage: Optional[int] = 10
    sort: Optional[str] = "created_at:desc"
    status: Optional[str]
    minPrice: Optional[int]
    maxPrice: Optional[int]
    category: Optional[List[int]] = None
    # 422 Unprocessable Entity
    # Optional은 None을 받을 수 있다는 의미이지 생략 가능한 것은 아니므로 기본값으로 None을 지정해 주어야 함
    seller: Optional[int]
    brand: Optional[int]
    inStock: Optional[bool]
    search: Optional[str]