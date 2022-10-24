from typing import Union
from pydantic import BaseModel

class ProductCreate(BaseModel):
    Product_name: str = Field(max_lenth=12)
    Price: int

class Product(BaseModel):
    # Product_id: int
    Product_name: str = Field(max_lenth=12)
    Price: int

    class Config:
        orm_mode = True