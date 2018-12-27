# Tree traversal
import queue


class Node:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.Value = value
        self.LeftChild = leftChild
        self.RightChild = rightChild

    def UpdateValue(self, newValue):
        self.Value = newValue

    def UpdateChildren(self, newNode, isLeft=True):
        if (isLeft):
            self.LeftChild = newNode
        else:
            self.RightChild = newNode

    def DeleteChildNode(self, isLeft=True):
        if (isLeft):
            self.LeftChild = None
        else:
            self.RightChild = None

#     4
#  2    6
# 1 3  5 7

# Breadth first search:
# 4, 2, 6, 1, 3, 5, 7

# Depth first search:
# 1, 2, 3, 4, 5, 6, 7


def BreadthFirstSearch(rootNode):
    # Uses a queue
    print("Breadth first search")
    q = queue.Queue()
    q.put(root)
    while(not q.empty()):
        node = q.get()
        if (node.LeftChild):
            q.put(node.LeftChild)
        if (node.RightChild):
            q.put(node.RightChild)
        print("Value: " + str(node.Value))


def DepthFirstSearch(rootNode):
    # Uses a stack
    print("Depth first search")


# Create a new tree
root = Node(4)
root.LeftChild = Node(2, Node(1), Node(3))
root.UpdateChildren(Node(6, Node(5), Node(7)), False)

BreadthFirstSearch(root)
