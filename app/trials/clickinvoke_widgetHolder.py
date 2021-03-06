import sys
import tkinter as tk
import tkinter.ttk as ttk



class ClickInvoke(tk.Tk):
    def __init__(self):
        super().__init__()
        self.b1 = ttk.Button(text='Button 1', name='b1', command=self.click1)
        self.b1.pack(side='left')
        self.b2 = ttk.Button(text='Button 2', name='b2', command=self.click2)
        self.b2.pack(side='left')

    def click1(self):
        print('Button 1 clicked.')

    def click2(self):
        print('Button 2 clicked.')
        self.b1.invoke()


def main():
    app = ClickInvoke()
    app.mainloop()


if __name__ == '__main__':
    sys.exit(main())