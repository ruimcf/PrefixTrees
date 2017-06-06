"""
Class node:
    @chr - The string that identifies the node

This is the base structure for a node in the Tree.
Attribute 'endOfWord' indicates if this node represents the end of a word.
Atribute children contains all the children nodes
"""
class node:
    def __init__(self, chr):
        self.char = chr
        self.children = []
        self.endOfWord = False


"""
Function find:
    @node - the starting node for the search
    @pattern - the pattern to be found in the tree.

For a pattern to be found, it must match with a sequence of nodes
in the tree, and the final node's @endOfWord must True
"""
def find(node, pattern):
    for letter in pattern:
        tamanho = len(node.children)
        if tamanho == 0:
            print("Not Found ", pattern)
            return
        for i in range(tamanho):
            if letter == node.children[i].char:
                if letter == pattern[-1]:
                    if node.children[i].endOfWord:
                        print("Found",pattern)
                        return
                    else:
                        print("Not Found", pattern)
                        return
                node = node.children[i]
                break
            else:
                if i == tamanho-1:
                    print("Not Found ", pattern)
                    return
    print("Found ", pattern)


"""
Function insertText:
    @cur_node: the first node of the tree
    @text: the text to be inserted in the tree

If the text consists of multiple words seperated by spaces,
each word will be inserted separately.
This calls insert function which inserts words as in a classic prefix tree.
"""
def insertText(cur_node, text):
    tokens = text.split(" ")
    for token in tokens:
        insert(cur_node, token.rstrip())


"""
Function insert:
    @cur_node: the first node of the tree
    @word: the word to be inserted

This function inserts the word in the tree as in a classic
prefix tree fashion, that is: only one character per node
"""
def insert(cur_node, word):
    k = 0
    for letter in word:
        k = k+1
        tamanho = len(cur_node.children)
        if tamanho == 0:
            new_node = node(letter)
            if(k == len(word)):
                new_node.endOfWord = True
            cur_node.children.append(new_node)
            cur_node = new_node
            print("Inserted letter ",letter)
        else:
            for i in range(tamanho):
                if letter == cur_node.children[i].char:
                    cur_node = cur_node.children[i]
                    if(k == len(word)):
                        cur_node.endOfWord = True
                    break
                else:
                    if i == tamanho-1:
                        new_node = node(letter)
                        if(k == len(word)):
                            new_node.endOfWord = True
                        cur_node.children.append(new_node)
                        cur_node = new_node
                        print("Inserted letter ",letter)
    print("Inserted word", word)


"""
Function remove:
    @root_node: the first node of the tree
    @word: the word to be removed from the tree

This function only works for prefix trees that contain
one character in each node.
This function starts the recursive function removeRecursive.
"""
def remove(root_node, word):
    removeRecursive(root_node, word, 0)


"""
Function removeRecursive:
    @cur_node: the current node in the tree
    @word: the word to be removed
    @i: represents how far we have travelled down

The function reaches the node that contains the end of the word
and then recursively deletes the necessary nodes until the top.
"""
def removeRecursive(cur_node, word, i):
    if i == len(word):
        if(len(cur_node.children) == 0):
            return 1
        else:
            cur_node.endOfWord = False
            return 0
    for j in range(len(cur_node.children)):
        if cur_node.children[j].char == word[i]:
            if(removeRecursive(cur_node.children[j], word, i+1)):
                del cur_node.children[j]
                if len(cur_node.children) == 0 and cur_node.endOfWord == False:
                    return 1
                else:
                    return 0
            else:
                return 0
    return 0


"""
Function printTree:
    @root_node: the first node of the tree

This function will call printRecursive which prints all
the words in the tree in a depth first search order.
"""
def printTree(root_node):
    print("####TREE####")
    queue = []
    for child in root_node.children:
        printRecursive(child, queue)


"""
Function printRecursive:
    @cur_node: the current node in the tree
    @queue: the current queue of nodes

The use of a queue allows to keep track of the
path - that is, the content of the word discovered so far.

print("".join(queue)) prints the content of the queue together.
"""
def printRecursive(cur_node, queue):
    queue.append(cur_node.char)
    if(len(cur_node.children) == 0):
        print("".join(queue))
        queue.pop()
        return
    if(cur_node.endOfWord == True):
        print("".join(queue))
    for child in cur_node.children:
        printRecursive(child, queue)
    queue.pop()



"""
Function printTreeNodes:
    @cur_node

This function prints the string of each node
in the tree, in a depth first search style.
"""
def printTreeNodes(cur_node):
    print(cur_node.char)
    for child in cur_node.children:
        printTreeNodes(child)



"""
Function insertRadix:
    @root_node: the first node of the tree
    @word: the word to be inserted

This function will call insertRadixRecursive which inserts
the word in the tree in a radix tree style - that is, a node
can contain more than one character
"""
def insertRadix(root_node, word):
    insertRadixRecursive(root_node, word, 0)


"""
Function insertRadixRecursive:
    @cur_node: the current node in the tree
    @word: the word to be inserted
    @letter: the current position in the word

This function may transform existing tree nodes in order
to insert a new word - splitting of a node.
Example:
    A node contains "Pratical" and we want to insert "Project"
    This will result in the transformation the node to "Pr"
    And nodes "atical" and "oject" to be added to its children.
"""
def insertRadixRecursive(cur_node, word, letter):
    tamanho = len(cur_node.children)
    if tamanho == 0:
        new_node = node(word[letter:])
        new_node.endOfWord = True
        cur_node.children.append(new_node)
        return
    for j in range(tamanho):
        child = cur_node.children[j]
        if child.char[0] == word[letter]:
            if(len(child.char) == 1):
                if(letter == len(word)-1):
                    child.endOfWord = True
                else:
                    insertRadixRecursive(child, word, letter+1)
                return
            else:
                for k in range(len(child.char)):
                    if child.char[k] == word[letter+k]:
                        if letter+k == len(word)-1:
                            if k == len(child.char)-1:
                                child.endOfWord = True
                                return
                            else:
                                split_node = node(child.char[k+1:])
                                child.char = child.char[:k+1]
                                split_node.children = child.children
                                split_node.endOfWord = child.endOfWord
                                child.endOfWord = False
                                child.children = []
                                child.children.append(split_node)
                                return
                    else:
                        split_node = node(child.char[k:])
                        child.char = child.char[:k]
                        split_node.children = child.children
                        split_node.endOfWord = child.endOfWord
                        child.endOfWord = False
                        child.children = []
                        child.children.append(split_node)
                        new_node = node(word[letter+k:])
                        new_node.endOfWord = True
                        child.children.append(new_node)
                        return
                insertRadixRecursive(child, word, letter+k+1)
                return
    new_node = node(word[letter:])
    new_node.endOfWord = True
    cur_node.children.append(new_node)
    return


"""
Function insertSuffixTree:
    @root: the first node in the tree
    @word: the word to be inserted

This function inserts into a Radix Tree
all the possible suffixes of the word.
"""
def insertSuffixTree(root, word):
    for i in range(len(word)):
        insertRadix(root, word[i:])




if __name__ == "__main__":
    #Create a new tree - root node
    root = node('')

    #Open input file - "inputText.txt" or "words.txt"
    fd = open("inputText.txt","r")

    #The number of lines to be inserted
    numberOfLines = 5

    #Insert numberOfLines lines in the tree
    #The method of insertion can be insertText | insertRadix | insertSuffixTree
    #rstrip() removes end of line character
    for line in range(numberOfLines):
        word = fd.readline().rstrip()
        if word != '':
            print("Inserting Word",word)
            insertSuffixTree(root, word)

    #Print Tree
    printTreeNodes(root)
    printTree(root)

