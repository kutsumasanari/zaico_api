from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Date
from .database import Base

class Product(Base):
    __tablename__ = 'products'
    
    product_name = Column(String, unique=True, index=True)
    price = Column(Integer, primary_key=True, index=True)
