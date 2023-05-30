import questionary
from menu import Menu
from user import User

class Controller:
    """プログラムの全体の流れを制御するクラス"""

    def __init__(self):
        self.user = User()
        self.menu = Menu(self.user)

    def start(self):
        
        while True:
            select_menu = self.menu.show_menulist()
            self.menu.execute_menuaction(select_menu)
            print("\n")