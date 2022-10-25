from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/create", response_model=schemas.Product)
async def create_products(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = crud.create_products(db=db, product=product)
    return product

# Read
@app.get("/read", response_model=List[schemas.Product])
async def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    product = crud.get_products(db, skip=skip, limit=limit)
    return product

# Update
# @app.put("/update", response_model=schemas.Product)
# async def update_products(product: schemas.ProductCreate, db: Session = Depends(get_db)):
#     return crud.update_products(db=db, product=product)

# # Delete
# @app.post("/delete", response_model=schemas.Product)
# async def delete_products(product: schemas.Product, db: Session = Depends(get_db)):
#     return crud.delete_products(db=db, product=product)

# @app.post("/rooms", response_model=schemas.Room)
# async def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
#     return crud.create_room(db=db, room=room)

# @app.post("/bookings", response_model=schemas.Booking)
# async def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
#     return crud.create_booking(db=db, booking=booking)

