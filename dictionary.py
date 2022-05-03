from red_black_tree import RedBlackTree


def load_file(tree, filename):
    file = open(filename, 'r')
    for each in file:
        insert_string(tree, each)


def insert_string(tree, string, mode=0):
    return tree.insert(string)


def search_file(tree, key):
    return tree.search(tree.root, key)
