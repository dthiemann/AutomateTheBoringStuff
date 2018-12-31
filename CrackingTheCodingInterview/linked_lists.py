# Chapter 2 - Linked Lists


class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def appendToTail(self, data):
        endNode = Node(data)
        n = self
        while (n.nextNode != None):
            n = n.nextNode
        n.nextNode = endNode

    def printLinkedList(self):
        dataList = [str(self.data)]
        currentNode = self
        while (currentNode.nextNode != None):
            currentNode = currentNode.nextNode
            dataList.append(str(currentNode.data))
        print(" - ".join(dataList))

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNextNode(self, newNode):
        self.nextNode = newNode


def removeDuplicates(startingNode):
    currentNode = startingNode
    while (currentNode != None and currentNode.getNext() != None):
        valueToCheck = currentNode.getData()
        runnerNode = currentNode
        while (runnerNode.getNext() != None):
            if (runnerNode.getNext().getData() == valueToCheck):
                runnerNode.setNextNode(runnerNode.getNext().getNext())
            else:
                runnerNode = runnerNode.getNext()
        currentNode = currentNode.getNext()

    startingNode.printLinkedList()


startingLink = Node(11)
startingLink.appendToTail(12)
startingLink.appendToTail(13)
startingLink.appendToTail(14)
startingLink.appendToTail(15)
startingLink.appendToTail(16)

startingLink.appendToTail(12)
startingLink.appendToTail(13)
startingLink.appendToTail(14)
startingLink.appendToTail(15)
startingLink.appendToTail(16)

print("starting list")
startingLink.printLinkedList()
print("ending list")
removeDuplicates(startingLink)
