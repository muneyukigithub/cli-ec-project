from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import ProductModel,ProductStockModel

engine = create_engine("mysql://root:password@db/ecDB")
Base = declarative_base()
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

saveitems1 = ProductStockModel(product_id=1,stock=10)
saveitems2 = ProductStockModel(product_id=2,stock=10)
saveitems3 = ProductStockModel(product_id=3,stock=10)
saveitems4 = ProductStockModel(product_id=4,stock=10)
saveitems5 = ProductStockModel(product_id=5,stock=10)

session.add(saveitems1)
session.add(saveitems2)
session.add(saveitems3)
session.add(saveitems4)
session.add(saveitems5)

session.commit()


# print(saveitems5.product)


# saveitems1 = ProductStockModel()

# saveitems1 = ProductModel(product="商品1",price=1000)


# saveitems2 = ProductModel(product="商品2",price=2000)
# saveitems3 = ProductModel(product="商品3",price=3000)
# saveitems4 = ProductModel(product="商品4",price=4000)
# saveitems5 = ProductModel(product="商品5",price=5000)



# session.add(saveitems1)
# session.add(saveitems2)
# session.add(saveitems3)
# session.add(saveitems4)
# session.add(saveitems5)



# session.commit()
