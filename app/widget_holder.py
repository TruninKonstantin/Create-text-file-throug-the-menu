import os

import tkinter as tk
import tkinter.ttk as ttk
import subprocess
from visualisation.part_previewer import PartPreviewer


class WidgetHolder(tk.Tk):
    # widgetList = []

    def __init__(self, master,pathToRootFolder):
        self.master = master
        self.widgetList = []
        self.create_first_row()
        self.create_row_for_data_after_current(0)
        self.pathToRootFolder = pathToRootFolder

    def create_first_row(self):
        label_00_01 = ttk.Label(self.master, text="Number")
        label_00_02 = ttk.Label(self.master, text="Length")
        # TODO align with radius in part previewer
        label_00_03 = ttk.Label(self.master, text="Diameter")
        label_00_04 = ttk.Label(self.master, text="AddAction")
        label_00_05 = ttk.Label(self.master, text="DelAction")
        label_00_06 = ttk.Button(self.master, text="Preview",
                                 command=lambda: self.preview_part())
        label_00_07 = ttk.Button(self.master, text="Print",
                                 command=lambda: self.print_file_with_data(self.pathToRootFolder))
        label_00_01.grid(row=0, column=0)
        label_00_02.grid(row=0, column=1)
        label_00_03.grid(row=0, column=2)
        label_00_04.grid(row=0, column=3)
        label_00_05.grid(row=0, column=4)
        label_00_06.grid(row=0, column=5)
        label_00_07.grid(row=0, column=6)
        self.widgetList.append([label_00_01, label_00_02, label_00_03, label_00_04, label_00_05])

    def create_row_for_data_after_current(self, indexOfLineWhereButtonPressed):
        rowIndexInList = int(indexOfLineWhereButtonPressed) + 1

        self.change_number_of_all_data_line(rowIndexInList)
        self.move_all_data_one_line_down(rowIndexInList)

        label_02_01 = ttk.Label(self.master, text=str(rowIndexInList))
        vcmd = self.master.register(self.validate)
        label_02_02 = ttk.Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))
        # label_02_02.insert(0, "Label " + str(rowIndexInList))
        label_02_03 = ttk.Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))
        # label_02_03.insert(0, "Label "+ str(rowIndexInList))

        label_02_04 = ttk.Button(self.master, text="Add",
                                 command=lambda: self.add_line_of_data_01(label_02_04))
        label_02_05 = ttk.Button(self.master, text="Del",
                                 command=lambda: self.del_line_of_data(label_02_05))

        label_02_01.grid(row=rowIndexInList, column=0)
        label_02_02.grid(row=rowIndexInList, column=1)
        label_02_03.grid(row=rowIndexInList, column=2)
        label_02_04.grid(row=rowIndexInList, column=3)
        label_02_05.grid(row=rowIndexInList, column=4)

        self.widgetList.insert(rowIndexInList,
                               [label_02_01, label_02_02, label_02_03, label_02_04, label_02_05])

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            return False

    def change_number_of_all_data_line(self, rowIndexInList):
        lenghtWidgetList = len(self.widgetList)
        for i in range(rowIndexInList, lenghtWidgetList):
            self.widgetList[i][0].config(text=str(i + 1))

    def move_all_data_one_line_down(self, rowIndexInList):
        lenghtWidgetList = len(self.widgetList)
        for i in range(rowIndexInList, lenghtWidgetList):
            for j in range(0, len(self.widgetList[i])):
                self.widgetList[i][j].grid(row=i + 1, column=j)

    def add_line_of_data_01(self, buttonObj):
        index_of_pressed_button = self.find_index_of_pressed_button(buttonObj)
        self.create_row_for_data_after_current(index_of_pressed_button)

    def find_index_of_pressed_button(self, buttonWidget):
        for i in range(0, len(self.widgetList)):
            for j in range(3, len(self.widgetList[i])):
                if id(buttonWidget) == id(self.widgetList[i][j]):
                    return i

    def del_line_of_data(self, buttonObj):
        if len(self.widgetList) > 2:

            index_of_pressed_button = self.find_index_of_pressed_button(buttonObj)
            # self.print_data_from_labels(index_of_pressed_button)

            # if index_of_pressed_button+1 >= len(self.widgetList):
            for j in range(0, len(self.widgetList[index_of_pressed_button])):
                self.widgetList[index_of_pressed_button][j].grid_forget()

            for i in range(index_of_pressed_button + 1, len(self.widgetList)):
                self.widgetList[i][0].config(text=str(i - 1))
                for j in range(0, len(self.widgetList[i])):
                    self.widgetList[i][j].grid(row=i - 1, column=j)

            # print("length " + str(len(self.widgetList)))
            # print("text " +str(len(self.widgetList[index_of_pressed_button][0].cget("text"))))
            del self.widgetList[index_of_pressed_button]
            # print("length " + str(len(self.widgetList)))
            # print("text " +str(len(self.widgetList[index_of_pressed_button][0].cget("text"))))
            # print(self.widgetList)

    # method is printing, but not deleting
    def print_data_from_labels(self, indexOfLineWhereButtonPressed):
        print(self.widgetList[indexOfLineWhereButtonPressed][1].get())

    def get_widget_list(self):
        return self.widgetList

    def preview_part(self):
        # pathToPython = r"E:\python\Python371\python.exe"
        # pathToVisualClass = r"e:\python\projects\create_text_file_through_the_menu\visualisation\pygame_trial_02.py"
        # startString= pathToPython + " " + pathToVisualClass
        #
        # subprocess.call(startString, shell=True)

        listOfParts = []

        for i in range(1, len(self.widgetList)):
            listOfParts.append([self.widgetList[i][1].get(), self.widgetList[i][2].get()])

        print(listOfParts)

        partPreviewer = PartPreviewer(listOfParts)
        partPreviewer.main()

    def print_file_with_data(self, pathToRootFolder):
        fileName = "resultFile.txt"
        join = os.path.join(pathToRootFolder, fileName)
        print (join)
        with open(join, "w") as text_file:

            for i in range(1, len(self.widgetList)):
                get = self.widgetList[i][1].get()
                get_1 = self.widgetList[i][2].get()
                string = str(get) + "    " + str(get_1) + "    " + "\n"
                text_file.write(string)
                print (str(get))

