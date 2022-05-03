from red_black_tree import RedBlackTree


def load_file(tree, filename):
    file = open(filename, 'r')
    for each in file:
        insert_str(tree, each)


def insert_str(tree, str, mode=0):
    if tree.insert(str) == -1:
        print("ERROR: Word already in the dictionary")
    if mode == 1:
        print("Height = " + str(tree.height(tree.root)))
        print("Size = " + str(tree.count))


dictionary = RedBlackTree()
load_file(dictionary, "EN-US-Dictionary.txt")
# tree.insert('Mariam')
# tree.insert('Aly')
# tree.insert('Nayrouz')
# tree.insert('Zawawy')
# tree.insert('Magdy')
# tree.insert('hamdy')
# tree.insert('ahmed')


print(str(dictionary.height(dictionary.root)))
print(str(dictionary.count))

insert_string(dictionary, 'Aly', 1)
insert_string(dictionary, 'Aly', 1)
