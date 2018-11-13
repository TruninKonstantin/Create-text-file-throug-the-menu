import logging
import os
import traceback
from tkinter import *
from tkinter import messagebox as tkMessageBox

from app.widget_holder import *

logFileName = "_log.txt"
pathToRoot = r"E:\python\projects\create_text_file_through_the_menu\app\trials"


root = Tk()
try:

    widgetHolder = WidgetHolder(root)

    root.mainloop()

except Exception as e:
    logging.exception(e)
    with open(os.path.join(pathToRoot, logFileName), "a") as file:
        file.write("\n\n***********************************************\n")
        file.write(traceback.format_exc())
        file.write("\n***********************************************\n\n")

    tkMessageBox.showerror(title="Please click Ok to continue",
                                    message="Something went wrong")