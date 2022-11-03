from sqlalchemy.orm import Session
from . import models, schemas

# 製品情報一覧取得（読み取り）
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

# 製品情報取得
def get_product(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.product_name==product_name).first()

# 製品情報登録
def create_product(db: Session, data: schemas.ProductCreate):
    db_product = models.Product(**data.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 製品情報更新
def update_product(db: Session, data: schemas.ProductUpdate):
    product = get_product(db, data.product_name)
    if product is None:
      return None
    for key, value in data:
        setattr(product, key, value)
    db.commit()
    return product

# 製品情報削除
def delete_product_name(db: Session, data: schemas.ProductDelete): # 製品名で
    db.query(models.Product).filter(models.Product.product_name == data.product_name).delete()
    db.commit()
    return None

