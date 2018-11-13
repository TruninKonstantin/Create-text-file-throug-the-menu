import unittest
from tkinter import *

from app.widget_holder import WidgetHolder


class UnittestWidgetHolder_check_del_last_line(unittest.TestCase):

    def setUp(self):
        self.master = Tk()
        self.widgetHolder = WidgetHolder(self.master)

    def test_click_button_row1_column4(self):
        self.widgetHolder.get_widget_list()[1][4].invoke()
        i = 2
        self.assertEqual(len(self.widgetHolder.get_widget_list()), i)

    if __name__ == "__main__":
        unittest.main()
