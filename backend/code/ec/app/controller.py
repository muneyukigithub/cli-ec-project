import questionary
from menu import Menu
from user import User

class Controller:
    """プログラムの全体の流れを制御するクラス"""

    def __init__(self):
        self.user = User()
        self.menu = Menu(self.user)

    def start(self):
        
        while self.menu.is_running:
            select_menu = self.menu.show_menulist()
            # if select_menu == "終了":
            #     break
            print(select_menu)
            self.menu.execute_menuaction(select_menu)
            print("\n")