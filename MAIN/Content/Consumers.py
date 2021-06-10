class Consumers:

    consumerList = []

    def addConsumer(self, name):
        self.consumerList.append(name)

    def getConsumer(self, id):
        return self.consumerList[id]

    def removeConsumer(self, id):
        self.consumerList.remove(self.consumerList[id])

