from Tkinter import Tk, Label, Button, StringVar


class Gui:

    widgetList = []

    def __init__(self, master, widgetList):
        self.master = master
        master.title("A simple GUI")
        self.widgetList = widgetList
