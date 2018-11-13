import unittest
from tkinter import *

from app.widget_holder import WidgetHolder


class UnittestWidgetHolder_Checking_widgetList_onClick(unittest.TestCase):

    def setUp(self):
        self.master = Tk()
        self.widgetHolder = WidgetHolder(self.master)
        self.widgetHolder.get_widget_list()[1][1].insert(0, "Label 01")
        self.widgetHolder.get_widget_list()[1][2].insert(0, "Label 02")

    def test_wiget_holder_content_row1_column0(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[1][0].cget("text"), "1")

    def test_wiget_holder_content_row1_column1(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[1][1].get(), "Label 01")

    def test_wiget_holder_content_row1_column2(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[1][2].get(), "Label 02")

    def test_click_button_row1_column3(self):
        self.widgetHolder.get_widget_list()[1][3].invoke()
        i = 3
        self.assertEqual(len(self.widgetHolder.get_widget_list()), i)

    if __name__ == "__main__":
        unittest.main()
