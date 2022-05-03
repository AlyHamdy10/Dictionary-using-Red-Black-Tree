from red_black_tree import RedBlackTree


def load_file(tree, filename):
    file = open(filename, 'r')
    for each in file:
        insert_string(tree, each)


def insert_string(tree, string, mode=0):
    if tree.insert(string) == -1:
        print("ERROR: Word already in the dictionary")
        return
    if mode == 1:
        print("Height = " + str(tree.height(tree.root)))
        print("Size = " + str(tree.count))





