import questionary
from questionary import Choice
from model import session,ProductModel,ProductStockModel,UserModel,CartModel
from sqlalchemy.exc import DatabaseError

class Cart:
    """カートを管理するクラス"""
    def __init__(self,user):
        self.user = user


    def displayproduct_in_cart(self):
        if not self.is_logged_in():
            print("ログインしてください")
            return 

        try:
            cartdata = self.get_cartdata()
        except Exception as e:
            print("エラー発生")

        self.show_cartdata(cartdata)


    def show_cartdata(self,cartdata):
        print("カートに入れた商品:")
        for cart, product, stock in cartdata:
            print(f"商品名: {product.product}, 価格: {product.price},注文数: {cart.quantity}")
        print("---")


    def deleteproduct_in_cart(self):
        if not self.is_logged_in():
            print("ログインしてください")
            return 

        try:
            cartdata = self.get_cartdata()
            cart_and_product = self.select_deleteproduct(cartdata)
            cart,product = cart_and_product
            self.deleteproduct(cart)  
            print(f"カートから{product.product}を削除しました")
        except DatabaseError as e:
            print(f"データベースエラーが発生しました:{str(e)}")
            return
        except Exception as e:
            print(f"エラーが発生しました:{str(e)}")
            return

    def select_deleteproduct(self,cartdata):
        print("カートに入れた商品:")
        product_list = [ Choice(title=f"商品名: {product.product}, 価格: {product.price},注文数: {cart.quantity}",value=(cart,product)) for cart, product, stock in cartdata ]
        cart_and_product = questionary.select('削除する商品を選択してください',choices=product_list).ask()
        return cart_and_product

    def deleteproduct(self,cart):
        try:
            cart = session.query(CartModel).filter_by(id=cart.id).first()
            session.delete(cart)
            session.commit()
        except DatabaseError as e:
            raise DatabaseError(f"エラーが発生しました{str(e)}")
        except Exception as e:
            raise Exception(f"エラーが発生しました{str(e)}")

    def is_logged_in(self):
        return self.user.username != "Guest"

    def get_cartdata(self):
        try:
            query_result = session.query(CartModel, ProductModel, ProductStockModel).\
                join(ProductModel, CartModel.product_id == ProductModel.id).\
                join(ProductStockModel, CartModel.product_id == ProductStockModel.product_id).\
                filter(CartModel.user_id == self.user.user_id).\
                all()
            return query_result

        except Exception as e:
            raise Exception(str(e))

