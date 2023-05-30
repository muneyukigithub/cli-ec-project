from abc import ABC,abstractmethod
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean,ForeignKey,UniqueConstraint
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:password@db/ecDB")
Base = declarative_base()
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()



# ユーザテーブル
class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(255),nullable=False)
    email = Column(String(255))
    username = Column(String(255),nullable=False)
    phonenumber = Column(String(255))
    is_active = Column(Integer,nullable=False)
    role = Column(Integer,nullable=False)
    last_login = Column(DateTime)
    created_at = Column(DateTime,default=datetime.now)

# 商品テーブル
class ProductModel(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product = Column(String(255),nullable=False,unique=True)
    price = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=datetime.now)

# 注文テーブル
class OrdersModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False)
    created_at = Column(DateTime,default=datetime.now)


# 注文明細テーブル
class OrdersDetailModel(Base):
    __tablename__ = "orders_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    orders_id = Column(Integer,ForeignKey('orders.id'),nullable=False)
    product_id = Column(Integer,ForeignKey('product.id'),nullable=False)
    quantity = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=datetime.now)


# 在庫テーブル
class ProductStockModel(Base):
    __tablename__ = "product_stock"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer,ForeignKey('product.id'),nullable=False,unique=True)
    stock = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=datetime.now)



# セッションテーブル
class SessionModel(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True,autoincrement=True)
    session_id = Column(String(255),nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False)
    expiration = Column(DateTime,nullable=False)
    created_at = Column(DateTime,default=datetime.now)

# カートテーブル
class CartModel(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True,autoincrement=True)
    product_id = Column(Integer,ForeignKey('product.id'),nullable=False)
    quantity = Column(Integer,nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False)
    created_at = Column(DateTime,default=datetime.now)

    __table_args__ = (
          UniqueConstraint('user_id', 'product_id', name='unique_user_product'),

    )

# テーブル自動生成メソッド
# python3 model.pyで使用
Base.metadata.create_all(engine)
