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
        return endNode

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

    def setData(self, newData):
        self.data = newData


# 1.1 Remove duplicates without a secondary data structure
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
startingLink.appendToTail(17)
startingLink.appendToTail(18)
nodeToRemove = startingLink.appendToTail(19)
startingLink.appendToTail(20)
startingLink.appendToTail(21)
startingLink.appendToTail(22)
startingLink.appendToTail(23)
startingLink.appendToTail(24)
startingLink.appendToTail(25)
startingLink.appendToTail(26)
startingLink.appendToTail(27)

# print("starting list")
# startingLink.printLinkedList()
# print("ending list")
# removeDuplicates(startingLink)

# 1.2 Find the kth from the last elemnt of a list


def findTheKthFromTheLast(startingNode, k):
    # Get the running node
    runner = startingNode
    current = startingNode
    i = 0
    while (runner.getNext() != None and i < k):
        runner = runner.getNext()
        i += 1

    if (i < k):
        return None     # The list is not long enough

    while (runner.getNext() != None):
        current = current.getNext()
        runner = runner.getNext()

    return current


# print(findTheKthFromTheLast(startingLink, 5).getData())

# 1.3 Delete an element from the middle of a singly linekd list with only access to that one element

def removeElementFromLinkedList(linkToDelete):
    if (linkToDelete == None or linkToDelete.getNext() == None):
        return None
    nextLink = linkToDelete.getNext()
    linkToDelete.setNextNode(nextLink.getNext())
    linkToDelete.setData(nextLink.getData())


startingLink.printLinkedList()
removeElementFromLinkedList(nodeToRemove)
startingLink.printLinkedList()
