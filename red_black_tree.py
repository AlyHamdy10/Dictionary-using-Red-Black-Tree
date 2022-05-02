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
        node.color = 1  # to be removed

        # fixing new node's attributes
        prev = None
        current = self.root

        while current != self.nill:
            prev = current
            comp = str_compare(node.word, current.word)
            if comp == 0:
                return -1       # Error Indicating word already exists
            elif comp == -1:
                current = current.left
            else:
                current = current.right

        node.parent = prev
        self.count += 1
        # fixing parents attributes
        if prev == None:
            self.root = node
        elif comp == -1:
            prev.left = node
        else:
            prev.right = node

        if node.parent == None:
            node.color = 0
            return 0

        if node.parent.parent == None:
            return 0
        self.fix_insert(node)
        return 0

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                uncle = k.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
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
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
            self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nill:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nill:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def print_inorder(self, node):
        if node != self.nill:
            self.print_inorder(node.left)
            print(str(node.word))
            self.print_inorder(node.right)

    def height(self, node):
        if node == self.nill:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


def str_compare(str1, str2):
    if isinstance(str1, int) and isinstance(str2, int):
        if str1 == str2:
            return 0
        elif str1 < str2:
            return -1
        return 1
    first = str1.lower()
    second = str2.lower()
    if first == second:
        return 0
    elif first < second:
        return -1
    return 1
