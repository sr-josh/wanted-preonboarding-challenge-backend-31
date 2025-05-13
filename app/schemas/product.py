from typing import List, Optional
from pydantic import BaseModel

class ProductQueryParams(BaseModel):
    page: Optional[int] = 1
    perPage: Optional[int] = 10
    sort: Optional[str] = "created_at:desc"
    status: Optional[str]
    minPrice: Optional[int]
    maxPrice: Optional[int]
    category: List[int]
    seller: Optional[int]
    brand: Optional[int]
    inStock: Optional[bool]
    search: Optional[str]