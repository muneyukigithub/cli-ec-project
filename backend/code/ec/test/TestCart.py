import unittest
from unittest.mock import Mock

import sys
sys.path.append("/code/ec/app")

from user import User
from cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.cart = Cart(self.user)


        return super().setUp()

    """
    ・self.is_logged_in()がTrueのときreturnされないこと
    ・self.is_logged_in()がFalseのときreturnされること
    ・self.is_logged_in()がTrueのとき、
        self.get_cartdata()が呼ばれること、
        self.show_cartdata(cartdata)が呼ばれること
    ・self.is_logged_in()がTrueで、
        cartdata = self.get_cartdata()でエラーが発生した場合、
        例外が発生しreturnされること
    """
    def test_displayproduct_in_cart(self):
        """
        self.is_logged_in()がTrueのとき、
        self.get_cartdata()が1回呼ばれること、
        self.show_cartdata(cartdata)が1回呼ばれること
        """

        mock_is_logged_in = Mock(return_value=True)
        self.cart.is_logged_in = mock_is_logged_in

        mock_get_cartdata = Mock()
        self.cart.get_cartdata = mock_get_cartdata

        mock_show_cartdata = Mock()
        self.cart.show_cartdata = mock_show_cartdata

        result = self.cart.displayproduct_in_cart()

        self.assertEqual(True,result)
        self.cart.get_cartdata.assert_called_once()
        self.cart.show_cartdata.assert_called_once()

    def test_displayproduct_in_cart_not_loggined(self):
        """
        self.is_logged_in()がFalseのときreturnされること
        """

        mock_is_logged_in = Mock(return_value=False)
        self.cart.is_logged_in = mock_is_logged_in

        result = self.cart.displayproduct_in_cart()

        self.assertEqual(False,result)

   

   


        #   mock_execute_menuaction = Mock(side_effect=self.controller.menu.execute_menuaction)
        # self.controller.menu.execute_menuaction = mock_execute_menuaction



        
