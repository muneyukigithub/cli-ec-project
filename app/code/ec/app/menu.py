import questionary
from questionary import Choice
from dataclasses import dataclass
from model import UserModel,session,ProductModel,ProductStockModel,CartModel,OrdersModel,OrdersDetailModel,SessionModel
from user import User
from auth import Auth
from shop import Shop
from cart import Cart
import sys

class Menu:
    """メニューを管理するクラス"""

    def __init__(self,user):
        self.user = user
        self.auth = Auth(user)
        self.shop = Shop(user)
        self.cart = Cart(user)

        self.menulist = {
            "サインアップ":self.auth.signup,
            "ログイン":self.auth.basic_login,
            "ログアウト":self.auth.logout,
            "商品選択":self.shop.selectproduct_to_cart,
            "商品購入":self.shop.order,
            "商品購入履歴":self.shop.order_history,
            "カート商品表示":self.cart.displayproduct_in_cart,
            "カート商品削除":self.cart.deleteproduct_in_cart,
            "終了":self.end}

    def show_menulist(self):
        select_menu = questionary.select(f'メニューを選択してください(現在{self.user.username}ユーザー)',choices=self.menulist.keys()).ask()
        return select_menu
        

    def execute_menuaction(self,select_menu):
        self.menulist[select_menu]()

    def end(self):
        print("お買い物を終了します")
        sys.exit(0)