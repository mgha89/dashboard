from app import db
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    role = Column(Integer(), nullable=False, default=2)
    name = Column(String(128), nullable=True, unique=False)
    phone = Column(String(11), nullable=True, unique=True)
    phone_auth = Column(Boolean(), default=False)
    active = Column(Boolean(), default=True)
    avatar = Column(String(150), default='')
    token = Column(String(150), default='')


    def __repr__(self) -> str:
        return f'{self.name} by {self.email}'


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def is_admin(self):
        return self.role == 0
