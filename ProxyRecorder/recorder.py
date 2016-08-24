class Recorder:

    def __init__(self):
        self._socketDetails = {}

    def createSocketPair(self, clientSocket, forwardSocket):
        self._socketDetails[clientSocket] = {
            "isForwardChannel": False,
            "socketPair": forwardSocket }

        self._socketDetails[forwardSocket] = {
            "isForwardChannel": True,
            "socketPair": clientSocket }

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

    def isForwardSocket(self, socID):
        return self.getSocketAttr(socID, "isForwardChannel")

    def getSocketPair(self, socID):
        return self.getSocketAttr(socID, "socketPair")

    def recordMessage(self, socID, data):
        pass
