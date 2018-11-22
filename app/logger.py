import os
from datetime import datetime


class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Logger:
    def __init__(self, pathToRootFolder):
        self.pathToRootFolder = pathToRootFolder
        self.logFileName = "_log.txt"
        self.pathToRootLogFile = os.path.join(pathToRootFolder, self.logFileName)
        self.counterForLog = 0
        self.printToLogFile("Start", "")

    def printToLogFile(self,comment, message):
        if self.counterForLog == 0:
            with open(self.pathToRootLogFile,"w") as text_file:
                text_file.write("%s \t %s \t\t\t\t %s\n" % (str(datetime.now()), comment, message))
                self.counterForLog +=1

        else:
            with open(self.pathToRootLogFile,"a") as text_file:
                text_file.write("%s \t %s \t\t\t\t %s\n" % (str(datetime.now()), comment, message))
                self.counterForLog +=1