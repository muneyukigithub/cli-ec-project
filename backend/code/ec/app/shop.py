import questionary
from model import session,ProductModel,ProductStockModel,UserModel,CartModel,OrdersModel,OrdersDetailModel
from sqlalchemy.exc import DatabaseError

class Shop:
    """買い物を管理するクラス"""
    def __init__(self,user):
        self.user = user

    # 商品選択
    def selectproduct_to_cart(self):
        if not self.is_logged_in():
            print("ログインしてください")
            return 

        try:
            select_product = self._get_productlist()
            product,product_stock = self._getmodel_product_and_stock(select_product)
            select_productstock = self._get_productstock(product.product,product_stock.stock)
            self._product_to_cart(product.id,select_productstock)
        except DatabaseError as e:
            print(f"データベースエラー")
        except Exception as e:
            print(f"エラー発生")

    def _get_productlist(self):
        items = session.query(ProductModel).all()
        return questionary.select('メニューを選択してください',choices=list(map(lambda x: x.product ,items))).ask()
    
    def _getmodel_product_and_stock(self,select_item):
        product,product_stock = session.query(ProductModel, ProductStockModel).join(ProductModel, ProductModel.id == ProductStockModel.product_id).filter(ProductModel.product == select_item).first()
        return product,product_stock
    
    def _get_productstock(self,product,productstock):

        print(f"{product}在庫数:{productstock}")
        return input("何個注文しますか？")

    def _product_to_cart(self,productid,select_productstock):
        user = session.query(UserModel).filter_by(username=self.user.username).first()

        try:
            cart = session.query(CartModel).filter_by(user_id=user.id,product_id=productid).first()
            if cart:
                cart.quantity = select_productstock
                session.commit()
            else:
                cartdata = {
                "product_id":productid,
                "quantity":select_productstock,
                "user_id":user.id,
                }
        
                new_cart = CartModel(**cartdata)
                session.add(new_cart)
                session.commit()
        except Exception as e:
            raise


    # 商品購入
    def order(self):

        if not self.is_logged_in():
            print("ログインしてください")
            return 

        cart = self.get_cart_items()        
     
        if len(cart) <= 0:
            print("カートに商品が入っていません")
            return

        order = self.create_order_record()
        if order:
            self.create_orderdetail_record(cart,order)
            print("商品購入が完了しました")
            return

        print("商品購入が失敗しました")
        
    
    def get_cart_items(self):
        return session.query(CartModel).filter_by(user_id=self.user.user_id).all()
        

    def create_orderdetail_record(self,cart,order):
        try:
            for cart_item in cart:
                order_detail = OrdersDetailModel(product_id=cart_item.product_id,quantity=cart_item.quantity,orders_id=order.id)
                session.add(order_detail)
                session.delete(cart_item)
            session.commit()
        except DatabaseError as e:
            print("データベースエラー発生")
        except Exception as e:
            print("エラー発生")

        
    def create_order_record(self):
        try:
            order = OrdersModel(user_id=self.user.user_id)
            session.add(order)
            session.commit()
            return order
        except DatabaseError as e:
            print("データベースエラー発生")
        except Exception as e:
            print("エラー発生")
        return None

    # 商品購入履歴
    def order_history(self):
        if not self.is_logged_in():
            print("ログインしてください")
            return 
            
        print(self.user.user_id,self.user.session_id,self.user.username)
        query_result = session.query(OrdersModel, OrdersDetailModel, ProductModel).\
            filter(OrdersModel.user_id == self.user.user_id).\
            join(OrdersDetailModel, OrdersModel.id == OrdersDetailModel.orders_id).\
            join(ProductModel, OrdersDetailModel.product_id == ProductModel.id).\
            all()

        print("注文番号 | 商品名 | 注文数 | 注文日時")
        for order,order_detail,product in query_result:
            print(f"{order.id} | {product.product} | {order_detail.quantity} | {order.created_at}")

        print("---")
  
    def is_logged_in(self):
        if self.user.username == "Guest":
                return False
        return True