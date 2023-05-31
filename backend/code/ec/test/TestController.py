
import sys
sys.path.append("/code/ec/app")


import unittest
from unittest.mock import patch, Mock
from controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_start_calls_methods_once(self):
        """
        show_menulistとexecute_menuactionが一度だけ呼び出されること 
        """
        mock_execute_menuaction = Mock(side_effect=self.controller.menu.execute_menuaction)
        self.controller.menu.execute_menuaction = mock_execute_menuaction

        mock_show_menulist = Mock(return_value='終了')

        self.controller.menu.show_menulist = mock_show_menulist

        self.controller.start()
        self.controller.menu.show_menulist.assert_called_once()
        self.controller.menu.execute_menuaction.assert_called_once()

if __name__ == '__main__':
    unittest.main()


