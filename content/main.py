from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import engine, SessionLocal

# Auto creation of database tables
models.Base.metadata.create_all(bind=engine)


# product_name のデータがデータベースに無い場合
class NoProductException(Exception):
    def __init__(self, name: str):
        self.name = name


# Application bootstrap
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# エラーハンドリング
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    if str("value_error.missing") in str(exc): # product_name, price が揃っていなかった場合
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error_code": "1"},
        )
    elif str("type_error.integer") in str(exc): # price の値が数字ではなかった場合
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error_code": "2"},
        )
    elif str("price must be plus") in str(exc): # price の値がマイナスだった場合
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error_code": "3"},
        )   

# エラーハンドリング、product_name のデータがデータベースに無い場合
@app.exception_handler(NoProductException)
async def no_product_exception_handler(request: Request, exc: NoProductException):
    return JSONResponse(
        status_code=222,
        content={"error_code": "4"}
    )


# 製品情報一覧取得（読み取り）
@app.get("/read", response_model=list[schemas.Product])
def products_action_get(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_products(db, skip=skip, limit=limit)
    return items

# 製品情報取得
@app.get("/read/{product_name}", response_model=schemas.Product)
def products_action_retrieve(product_name: str, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_name)
    if product is None:
        raise HTTPException(status_code=404)
    return product


# 製品情報登録
@app.post("/create", response_model=schemas.ProductCreate)
def product_action_create(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, data.product_name) # 同じ product_name のデータがデータベースに既に入っているのか
    if db_product is None: # 新しいレコードを追加する
        product = crud.create_product(db, data)
    else: # レコードを追加せず入力された price で値を更新する
        product = crud.update_product(db, data)
    return product
    

# 製品情報更新
@app.post("/update", response_model=schemas.Product)
def products_action_update(data: schemas.ProductUpdate,  db: Session = Depends(get_db)):
    product = crud.update_product(db, data)
    if product is None:
        raise HTTPException(status_code=404)
    return product


# 製品情報削除
@app.post("/delete", status_code=204) # 製品名で
def products_action_delete_name(data: schemas.ProductDelete,  db: Session = Depends(get_db)):
    db_product = crud.get_product(db, data.product_name)  # product_name のデータがデータベースにあるのか
    if db_product is None:
        raise NoProductException(name=data.product_name)    
    else:
        crud.delete_product_name(db, data)
    return None

