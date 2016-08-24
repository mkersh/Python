import sys
import os
import pdb

def _getPropertyValue(line):
    parts = line.split(":")
    return (parts[0].lower(), parts[1].strip())

class Config:
    def __init__(self, filePath=None):
        basedir = os.path.dirname(os.path.abspath(__file__))
        if filePath is None:
            self.configFilePath = basedir + r"/Config.txt"
        elif os.path.isfile(filePath):
            self.configFilePath = filePath
        else:
            fp = basedir + r"/" + filePath
            if os.path.isfile(fp):
                self.configFilePath = fp
            else:
                assert False, "Cannot locate Config File: {}".format(filePath)


    def getRecordingSetting(self, recName):
        foundSection = False
        f = open(self.configFilePath,"r")
        recObject = {}
        recObject["messages"] = []
        currentObj = recObject
        for line in f.readlines():
            prop, value = _getPropertyValue(line)
            if prop == "section":
                if foundSection == True:
                    break
                elif value == recName:
                    foundSection = True
                    currentObj["name"] = recName
            elif foundSection == True:
                if prop == "message":
                    currentObj = {}
                    recObject["messages"].append(currentObj)
                    currentObj["name"] = value
                else:
                    currentObj[prop] = value
        self._recSettings = recObject
        return recObject

