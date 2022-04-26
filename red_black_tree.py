# Implementation of Red-Black Tree in python


class Node():
    def __init__(self, word):
        self.word = word
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.nill = Node(0)  # creation of the NILL node
        self.nill.color = 0  # setting the NILL node's color as black
        self.root = self.nill  # setting the RBTree's root as NILL as it is empty
        self.count = 0
        # some attributes were not added here since they were added in node declaration
