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
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                uncle = k.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    k.parent = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        # function to right_rotate(k)
                    # to be done
            else:
                uncle = k.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        #function to left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    #function to right_rotate(k.parent.parent)
            if k == self.root:
                break
            self.root.color = 0
