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


def removeDuplicates(startingNode):
    currentNode = startingNode
    while (currentNode.nextNode != None):
        currentValue = currentNode.getData()

        # Search rest of the list removing any elements that match
