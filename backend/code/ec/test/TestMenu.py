import sys
sys.path.append("/code/ec/app")
from questionary import Choice

from io import StringIO
import unittest
from unittest.mock import Mock,patch
from menu import Menu
from user import User

class MenuTestCase(unittest.TestCase):
    def setUp(self):
        self.user = Mock()  # テスト用のユーザーオブジェクトを作成
        self.menu = Menu(self.user)

    def test_show_menulist_select_end(self):
        """選択したメニューの文字列が戻り値として返ること"""
        selected_menu = self.menu.show_menulist()
        self.assertEqual(selected_menu, "終了")

    def test_execute_menuaction(self):
        """メニューアクションが1回だけ実行されること"""
        test_select_menu = "終了"
        self.menu.menulist[test_select_menu] = Mock()

        self.menu.execute_menuaction(test_select_menu)
        self.menu.menulist[test_select_menu].assert_called_once()

if __name__ == '__main__':
    unittest.main()


# questionary.selectをモックし、終了が選択された場合の動作をシミュレートする
# with patch('menu.questionary.select') as mock_select:
# mock_select.return_value = "終了"
# mock_select.assert_called_once()


# class TestMenu(unittest.TestCase):
#     def setUp(self):
#         self.user = User("John") 
#         self.menu_obj = Menu(self.user)

#     def test_show_menulist(self):
#         """
#         メニューが正しく表示されるか
#         """
        
#         expected_output = 'メニューを選択してください(現在Johnユーザー): '
#         user_input = 'ログアウト'  # ユーザーが選択するメニューの入力

#         with patch('builtins.input', side_effect=[user_input]), patch('sys.stdout', new=StringIO()) as fake_out:
#             select_menu = self.menu_obj.show_menulist()
#             self.assertEqual(fake_out.getvalue(), expected_output)
#             self.assertEqual(select_menu, user_input)



        # self.your_obj.menulist = {'1': 'ハンバーガー', '2': 'ピザ', '3': 'サンドイッチ'}

        # expected_output = 'メニューを選択してください(現在Johnユーザー): '
        
        # with patch('sys.stdout', new=StringIO()) as fake_out:
        #     self.menu.show_menulist()
            # print(fake_out.getvalue().strip())
            # self.assertEqual(fake_out.getvalue().strip(), expected_output)

