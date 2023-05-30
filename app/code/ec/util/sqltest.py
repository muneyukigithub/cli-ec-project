from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import *

engine = create_engine("mysql://root:password@db/ecDB")
Base = declarative_base()
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()


        # query_result = session.query(CartModel, ProductModel, ProductStockModel).\
        # join(ProductModel, CartModel.product_id == ProductModel.id).\
        # join(ProductStockModel, CartModel.product_id == ProductStockModel.product_id).\
        # filter(CartModel.user_id == self.user.user_id).\
        # all()

# query_result = session.query(OrdersModel, OrdersDetailModel,ProductModel).\
# join(OrdersModel, OrdersModel.id == OrdersDetailModel.orders_id).\
# join(OrdersDetailModel,OrdersDetailModel.product_id==ProductModel.id).\
# all()

query_result = session.query(OrdersModel, OrdersDetailModel, ProductModel).\
    join(OrdersDetailModel, OrdersModel.id == OrdersDetailModel.orders_id).\
    join(ProductModel, OrdersDetailModel.product_id == ProductModel.id).\
    all()

print("注文番号 | 商品名 | 注文数 | 注文日時")
for order,order_detail,product in query_result:
    print(f"{order.id} | {product.product} | {order_detail.quantity} | {order.created_at}")
    # print(f"注文i_{order.id} : 商品名{product.product} , 注文数:{order_detail.quantity}")

print("---")
# join(ProductStockModel, CartModel.product_id == ProductStockModel.product_id).\
# filter(CartModel.user_id == self.user.user_id).\
# all()


# getuser_query = session.query(UserModel).filter_by(username="admin")
# user = getuser_query.first()
# print(user.id)


# ユーザテーブル
# class UserModel(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     password = Column(String(255),nullable=False)
#     email = Column(String(255))
#     username = Column(String(255),nullable=False)
#     phonenumber = Column(String(255))
#     is_active = Column(Integer,nullable=False)
#     role = Column(Integer,nullable=False)
#     last_login = Column(DateTime)
#     created_at = Column(DateTime,default=datetime.now)

# class ExistingUser(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True)
#     password = Column(String,nullable=False)
#     email = Column(String)
#     username = Column(String)
#     phonenumber = Column(String)
#     is_active = Column(Integer)
#     role = Column(Integer)
#     last_login = Column(DateTime)
#     created_at = Column(DateTime,default=datetime.now)

# session_id = str(uuid.uuid4())
# getuser_query = UserModel(username="admin")
# print(login_user.username)

# users = session.query(ExistingUser).all()
# for user in users:
#     print(dir(user))
#     print(user.created_at)


# # MySQLdbのインポート
# import MySQLdb
 
# # データベースへの接続とカーソルの生成
# connection = MySQLdb.connect(
#     host='db',
#     user='root',
#     passwd='password',
#     db='ecDB')
# cursor = connection.cursor()
 
# # ここに実行したいコードを入力します
# #cursor.execute("insert into user values(1,"password","admin@admin.com","admin","99988887777",0,0,"2023-05-21 13:45:30")")
# cursor.execute('INSERT INTO user (id, password, email, username, phonenumber, is_active, role, last_login, created_at) VALUES (1, "password", "admin@admin.com", "admin", "99988887777", 0, 0, "2023-05-21 13:45:30", CURRENT_TIMESTAMP)')


# # 保存を実行
# connection.commit()
 
# # 接続を閉じる
# connection.close()

# # INSERT INTO user (id, password, email, username, phonenumber, is_active, role, last_login, created_at) VALUES (2, "password", "user01@user.com", "user01", "99988887777", 0, 0, "2023-05-21 13:45:30", CURRENT_TIMESTAMP)