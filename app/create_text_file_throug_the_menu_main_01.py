import logging
import os
import traceback
from tkinter import *
from tkinter import messagebox as tkMessageBox
from app.logger import Logger

from app.widget_holder import *

logFileName = "_log.txt"
pathToRootFolder = r"D:\Code_Storage\python\projects\create_text_file_through_the_menu\app\trials"


root = Tk()
logger = Logger(pathToRootFolder)
try:

    widgetHolder = WidgetHolder(root,pathToRootFolder)

    root.mainloop()

except Exception as e:
    logging.exception(e)
    with open(logger.pathToRootLogFile, "a") as file:
        file.write("\n\n***********************************************\n")
        file.write(traceback.format_exc())
        file.write("\n***********************************************\n\n")

    tkMessageBox.showerror(title="Please click Ok to continue",
                                    message="Something went wrong")