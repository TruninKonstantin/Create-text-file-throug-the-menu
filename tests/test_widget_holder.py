import tkinter.ttk as ttk
import unittest
from tkinter import *

from app.widget_holder import WidgetHolder


class UnittestWidgetHolder_Checking_widgetList(unittest.TestCase):

    def setUp(self):
        self.master = Tk()
        self.widgetHolder = WidgetHolder(self.master)

    def test_widget_List_length_is_equal_to_two(self):
        i = 2
        self.assertEqual(len(self.widgetHolder.get_widget_list()), i)

    def test_label_number_row0_column0_is_instance_of_Label(self):
        widget = self.widgetHolder.get_widget_list()[0][0]
        self.assertIsInstance(widget, ttk.Label)

    def test_label_number_row0_column0_widget_text_equal_number(self):
        widget = self.widgetHolder.get_widget_list()[0][0]
        assert widget.cget("text") == "Number"

    def test_label_Length_row0_column1_is_instance_of_Label(self):
        widget = self.widgetHolder.get_widget_list()[0][1]
        self.assertIsInstance(widget, ttk.Label)

    def test_label_Length_row0_column1_widget_text_equal_Length(self):
        widget = self.widgetHolder.get_widget_list()[0][1]
        assert widget.cget("text") == "Length"

    def test_label_Diameter_row0_column2_is_instance_of_Label(self):
        widget = self.widgetHolder.get_widget_list()[0][2]
        self.assertIsInstance(widget, ttk.Label)

    def test_label_Diameter_row0_column2_widget_text_equal_Diameter(self):
        widget = self.widgetHolder.get_widget_list()[0][2]
        assert widget.cget("text") == "Diameter"

    def test_label_AddAction_row0_column3_is_instance_of_Label(self):
        widget = self.widgetHolder.get_widget_list()[0][3]
        self.assertIsInstance(widget, ttk.Label)

    def test_label_AddAction_row0_column3_widget_text_equal_AddAction(self):
        widget = self.widgetHolder.get_widget_list()[0][3]
        assert widget.cget("text") == "AddAction"

    def test_label_DelAction_row0_column4_is_instance_of_Label(self):
        widget = self.widgetHolder.get_widget_list()[0][4]
        self.assertIsInstance(widget, ttk.Label)

    def test_label_DelAction_row0_column4_widget_text_equal_DelAction(self):
        widget = self.widgetHolder.get_widget_list()[0][4]
        assert widget.cget("text") == "DelAction"




    def test_label_number_row1_column0_is_instance_of_Label(self):
        widget = self.widgetHolder.get_widget_list()[1][0]
        self.assertIsInstance(widget, ttk.Label)

    def test_label_number_row1_column0_widget_text_equal_number(self):
        widget = self.widgetHolder.get_widget_list()[1][0]
        assert widget.cget("text") == "1"

    def test_label_entry_row1_column1_is_instance_of_Entry(self):
        widget = self.widgetHolder.get_widget_list()[1][1]
        self.assertIsInstance(widget, ttk.Entry)

    def test_label_entry_row1_column1_widget_text_equal_empty(self):
        widget = self.widgetHolder.get_widget_list()[1][1]
        assert widget.cget("text") == ""

    def test_label_entry_row1_column2_is_instance_of_Entry(self):
        widget = self.widgetHolder.get_widget_list()[1][2]
        self.assertIsInstance(widget, ttk.Entry)

    def test_label_entry_row1_column2_widget_text_equal_empty(self):
        widget = self.widgetHolder.get_widget_list()[1][2]
        assert widget.cget("text") == ""

    def test_button_Add_row1_column3_is_instance_of_Button(self):
        widget = self.widgetHolder.get_widget_list()[1][3]
        self.assertIsInstance(widget, ttk.Button)

    def test_button_Add_row1_column3_widget_button_text_equal_Add(self):
        widget = self.widgetHolder.get_widget_list()[1][3]
        assert widget.cget("text") == "Add"

    def test_button_Del_row1_column4_is_instance_of_Button(self):
        widget = self.widgetHolder.get_widget_list()[1][4]
        self.assertIsInstance(widget, ttk.Button)

    def test_button_Del_row1_column4_widget_button_text_equal_Del(self):
        widget = self.widgetHolder.get_widget_list()[1][4]
        assert widget.cget("text") == "Del"




    if __name__ == "__main__":
        unittest.main()
