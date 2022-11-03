from pydantic import BaseModel, ValidationError, validator

class ProductCreate(BaseModel):
    product_name: str 
    price: int
        
    class Config:
        orm_mode = True
    
    # エラー設定、price の値がマイナスだった場合
    @validator('price')
    def price_must_be_plus(cls, v):
        if v < 0:
            raise ValueError('price must be plus')
        return v
    
class ProductUpdate(BaseModel):
    product_name: str 
    price: int

    # エラー設定、price の値がマイナスだった場合
    @validator('price')
    def price_must_be_plus(cls, v):
        if v < 0:
            raise ValueError('price must be plus')
        return v

class ProductDelete(BaseModel):
    product_name: str 

class Product(ProductCreate):
    product_id: int
    
    class Config:
        orm_mode = True
