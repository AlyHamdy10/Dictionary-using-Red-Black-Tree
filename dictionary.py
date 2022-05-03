from red_black_tree import RedBlackTree


def load_file(tree, filename):
    print("-"*10 + "Loading \"" + filename + "\" into Dictionary" + "-"*10)
    file = open(filename, 'r')
    for each in file:
        insert_string(tree, each)
    print('Tree Height = ' + str(tree.height(dictionary.root)))
    print('Tree size = ' + str(tree.count))
    print("-"*10 + "Loading Complete" + "-"*10 + "\n")


def insert_string(tree, string, mode=0):
    r = tree.insert(string)
    if mode == 1:
        print("-"*10 + "Inserting \"" + string + "\" into Dictionary" + "-"*10)
        if r == -1:
            print(">" * 5 + "ERROR: Word already in the dictionary" + "<"*5)
            print("-"*10 + "Insertion Failed" + "-"*10 + "\n")
        else:
            print("Height = " + str(tree.height(tree.root)))
            print("Size = " + str(tree.count))
            print("-"*10 + "Insertion Complete" + "-"*10 + "\n")


def search_file(tree, key):
    print("-"*10 + "Searching for \"" + key + "\" in Dictionary" + "-"*10)
    hold = tree.search(tree.root, key)
    if hold == tree.nill:
        print(">"*5 + "NOT FOUND" + "<"*5)
    else:
        print(">"*5 + "FOUND" + "<"*5)
    print("-"*10 + "Search Complete" + "-"*10 + "\n")


dictionary = RedBlackTree()
load_file(dictionary, "EN-US-Dictionary.txt")

insert_string(dictionary, 'Mariam', 1)
insert_string(dictionary, 'Mariam', 1)
search_file(dictionary, 'Fargo')
insert_string(dictionary, 'Fargo', 1)
search_file(dictionary, 'Fargo')
