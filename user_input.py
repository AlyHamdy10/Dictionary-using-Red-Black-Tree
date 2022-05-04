from dictionary import *
from red_black_tree import RedBlackTree


def load(tree, filename="EN-US-Dictionary.txt"):
    print_dash("Loading \"" + filename + "\" into Dictionary")
    load_file(tree, filename)
    print_properties(dictionary)
    file = open(filename, 'r')
    for each in file:
        dictionary.insert(each)
    print_properties(tree)
    print_dash("Loading Complete", 1)


def insert(tree, string):
    print("-"*10 + "Inserting \"" + string + "\" into Dictionary" + "-"*10)
    r = dictionary.search(dictionary.root, string)
    if r == -1:
        print_arrow("ERROR: Word already in the dictionary")
        print_dash("Insertion Failed", 1)
    else:
        print_properties(tree)
        print_dash("Insertion Complete", 1)


def search(tree, key):
    print_dash("Searching for \"" + key + "\" in Dictionary")
    hold = dictionary.search(tree.root, key)
    if hold == tree.nill:
        print_arrow("NOT FOUND")
    else:
        print_arrow("FOUND")
    print_dash("Search Complete", 1)


def print_properties(tree):
    print('Tree Height = ' + str(tree.height(tree.root)))
    print('Tree size = ' + str(tree.count))


def print_dash(string, newline=0):
    print("-"*10 + string + "-"*10)
    if newline == 1:
        print()


def print_arrow(string):
    print(">" * 5 + string + "<"*5)


def options():
    string = """
    Enter Operation:
    1 > Load Dictionary
    2 > insert in Dictionary
    3 > Search in Dictionary
    0 > End
    """
    return int(input(string))


dictionary = RedBlackTree()
loaded = 0
mode = -1
while mode != 0:
    mode = options()

    if mode == 1:
        if loaded == 1:
            print_dash("Dictionary Already Loaded")
        else:
            load(dictionary)
            loaded = 1
        continue
    elif mode == 2:
        string = input("Enter Word to be Added to Dictionary: ")
        insert(dictionary, string)
        continue
    elif mode == 3:
        key = input("Enter Word to be Searched for in Dictionary: ")
        search(dictionary, key)
        continue

print_dash("Program End")
