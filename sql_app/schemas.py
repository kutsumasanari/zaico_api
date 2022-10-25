from typing import Union
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    product_name: str = Field(max_lenth=12)
    price: int

class Product(ProductCreate):
    product_id: int

    class Config:
        orm_mode = True
