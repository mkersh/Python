import configFile as config

class Recorder:

    def __init__(self, configFile = None):
        self._socketDetails = {}
        self._config = config.Config(configFile)

    def getConfig(self):
        return self._config

    def createSocketPair(self, clientSocket, forwardSocket):
        self._socketDetails[clientSocket] = {
            "isForwardChannel": False,
            "socketPair": forwardSocket,
            "data": None }

        self._socketDetails[forwardSocket] = {
            "isForwardChannel": True,
            "socketPair": clientSocket,
            "data": None }

    def socketCount(self):
        return len(self._socketDetails)

    def closeSocket(self, socID):
        pairedSocket = self.getSocketPair(socID)
        del self._socketDetails[socID]
        del self._socketDetails[pairedSocket]

    def _getSocketDetails(self, socID):
        return self._socketDetails[socID]

    def getSocketAttr(self, socID, attr):
        socDetails = self._getSocketDetails(socID)
        return socDetails[attr]

    def setSocketAttr(self, socID, attr, value):
        socDetails = self._getSocketDetails(socID)
        socDetails[attr] = value

    def isForwardSocket(self, socID):
        return self.getSocketAttr(socID, "isForwardChannel")

    def getSocketPair(self, socID):
        return self.getSocketAttr(socID, "socketPair")

    def getSocketData(self, socID):
        return self.getSocketAttr(socID, "data")

    def appendSocketData(self, socID, newData):
        data = self.getSocketAttr(socID, "data")
        if data is None:
            data = newData
        else:
            data += newData
        self.setSocketAttr(socID, "data", data)

    def recordMessage(self, sendToSoc, data):
        if self.isForwardSocket(sendToSoc):
            self.recordResponseMessage(sendToSoc, data)
        else:
            self.recordRequestMessage(sendToSoc, data)

    def recordRequestMessage(self, sendToSoc, data):
        self.appendSocketData(sendToSoc, data)

    def recordResponseMessage(self, sendToSoc, data):
        self.appendSocketData(sendToSoc, data)
        self.saveServiceCall(sendToSoc)

    def saveServiceCall(self, responseSocket):
        requestSocket = self.getSocketPair(responseSocket)
        requestData = self.getSocketData(requestSocket)
        responseData = self.getSocketData(responseSocket)
        # NOTE: suspect that responseData could come back in chunks
        self.createAndStoreFiles(requestData, responseData)

    def createAndStoreFiles(self, requestData, responseData):
        pass
