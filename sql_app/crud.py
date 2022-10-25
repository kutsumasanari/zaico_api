from sqlalchemy.orm import Session
from sql_app import models, schemas

# 製品情報登録
def create_products(db: Session, product: schemas.Product):
    db_product = models.Product(product_name=product.product_name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 製品情報取得
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

# # 製品情報更新
# def update_products(db: Session, product: schemas.Product):
#     query = db.update().where(db.columns.Product_name==product.Product_name)
#     ret = db.execute(query)
#     return {**product.dict()}

# # 製品情報削除
# def delete_products(db: Session, product: schemas.Product):
#     query = db.delete().where(db.columns.Product_name==product.Product_name)
#     ret = db.execute(query)
#     return {"result": "delete success"}
