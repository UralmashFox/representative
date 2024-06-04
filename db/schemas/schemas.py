from sqlalchemy import Column, ForeignKey, BigInteger, VARCHAR

from db.base_class import Base


class Product(Base):
    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(length=255), unique=False)
    cost = Column(VARCHAR(length=255), unique=False)


class User(Base):
    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(length=255), unique=False)


class UserProduct(Base):
    user_id = Column(BigInteger, ForeignKey('user.id'), primary_key=True)
    product_id = Column(BigInteger, ForeignKey('product.id'), primary_key=True)
