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
    def insert(self, word):
        node = Node(word)
        node.left = self.nill
        node.right = self.nill
        node.color = 1

        # fixing new node's attributes
        prev = None
        current = self.root

        while current != self.Nill:
            prev = current
            if node.word.lower == current.word.lower:
                return -1       # Error Indicating word already exists
            elif node.word.lower < current.word.lower:
                current = current.left
            else:
                current = current.right

        node.parent = prev
        self.count += 1
        # fixing parents attributes
        if prev == None:
            self.root = node
        elif node.word.lower < prev.word.lower:
            prev.left = node
        else:
            prev.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return
        # function to fix rbtree due to insert
