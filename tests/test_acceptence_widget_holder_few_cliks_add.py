import unittest
from tkinter import *

from app.widget_holder import WidgetHolder


class UnittestWidgetHolder_Acceptence_few_click_add(unittest.TestCase):

    def setUp(self):
        self.master = Tk()
        self.widgetHolder = WidgetHolder(self.master)
        self.widgetHolder.get_widget_list()[1][1].insert(0, "01.01")
        self.widgetHolder.get_widget_list()[1][2].insert(0, "01.02")
        self.widgetHolder.get_widget_list()[1][3].invoke()
        self.widgetHolder.get_widget_list()[2][1].insert(0, "02.01")
        self.widgetHolder.get_widget_list()[2][2].insert(0, "02.02")
        self.widgetHolder.get_widget_list()[1][3].invoke()
        self.widgetHolder.get_widget_list()[2][3].invoke()
        self.widgetHolder.get_widget_list()[4][3].invoke()

    def test_wiget_holder_content_row1_column0(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[1][0].cget("text"), "1")

    def test_wiget_holder_content_row1_column1(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[1][1].get(), "01.01")

    def test_wiget_holder_content_row1_column2(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[1][2].get(), "01.02")

    def test_wiget_holder_content_row2_column0(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[2][0].cget("text"), "2")

    def test_wiget_holder_content_row2_column1(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[2][1].get(), "")

    def test_wiget_holder_content_row2_column2(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[2][2].get(), "")

    def test_wiget_holder_content_row3_column0(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[3][0].cget("text"), "3")

    def test_wiget_holder_content_row3_column1(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[3][1].get(), "")

    def test_wiget_holder_content_row3_column2(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[3][2].get(), "")

    def test_wiget_holder_content_row4_column0(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[4][0].cget("text"), "4")

    def test_wiget_holder_content_row4_column1(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[4][1].get(), "02.01")

    def test_wiget_holder_content_row4_column2(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[4][2].get(), "02.02")

    def test_wiget_holder_content_row5_column0(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[5][0].cget("text"), "5")

    def test_wiget_holder_content_row5_column1(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[5][1].get(), "")

    def test_wiget_holder_content_row5_column2(self):
        self.assertEqual(self.widgetHolder.get_widget_list()[5][2].get(), "")

    if __name__ == "__main__":
        unittest.main()
