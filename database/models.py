from database import Base
from sqlalchemy import Column, String, ForeignKey, Integer, BigInteger, DateTime
from sqlalchemy_utils import PasswordType
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

class User(Base):
    __tablename__ = 'auth.user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256), unique=False, nullable=False)

    advertisements = relationship("Advertisement", back_populates='owner')
    offers = relationship("Offer", back_populates='user')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


def default_end_time():
    end_time = datetime.now()
    end_time += timedelta(days=7)
    return end_time


class Advertisement(Base):
    __tablename__ = 'sale.advertisement'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('auth.user.id'))
    owner = relationship("User", back_populates="advertisements")
    title = Column(String(64))
    description = Column(String(256))
    car_name = Column(String(64))
    car_model = Column(String(64))
    min_price = Column(BigInteger)
    end_time = Column(DateTime(), default=default_end_time)

    offers = relationship('Offer', back_populates='advertisement')

class Offer(Base):
    __tablename__ = 'sale.offer'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('auth.user.id'))
    user = relationship("User", back_populates="offers")
    advertisement_id = Column(Integer, ForeignKey('sale.advertisement.id'))
    advertisement = relationship("Advertisement", back_populates="offers")
    price = Column(BigInteger, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)

