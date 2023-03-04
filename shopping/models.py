from jdatetime import datetime
from app import db
from sqlalchemy import Column, ForeignKey, Text, Integer, String, Boolean, DateTime, event, Table, DECIMAL
from auth.models import User



class Product(db.Model):
    __tablename__ = 'shopping_products'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Integer(), default=0)
    category_id = Column(Integer(), ForeignKey('shopping_categories.id'))
    number = Column(Integer(), default=0)
    image = Column(String(100), default='img/product.jpg')
    date = Column(DateTime(), default=datetime.now())
    rating = Column(db.DECIMAL(8, 2), default=1.0)

    def __repr__(self) -> str:
        return self.name
    
    def is_available(self):
        return True if len(self.number) > 0 else False 
    
    def category(self):
        return Category.query.get(self.category_id).name
    



class Category(db.Model):
    __tablename__ = 'shopping_categories'
    id = Column(Integer(), primary_key=True)    
    title = Column(String(100), nullable=False, unique=True)
    date = Column(DateTime(), default=datetime.now())

    def __repr__(self) -> str:
        return self.title
    





