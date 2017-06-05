class node:
    def __init__(self, chr):
        self.char = chr
        self.children = []
        self.endOfWord = False


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


def insertText(cur_node, text):
    tokens = text.split(" ")
    for token in tokens:
        insert(cur_node, token)

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

def remove(cur_node, word):
    removeRecursive(cur_node, word, 0)

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


def printTree(root_node):
    print("####TREE####")
    stack = []
    for child in root_node.children:
        printRecursive(child, stack)

def printRecursive(cur_node, stack):
    stack.append(cur_node.char)
    if(len(cur_node.children) == 0):
        print("".join(stack))
        stack.pop()
        return
    if(cur_node.endOfWord == True):
        print("".join(stack))
    for child in cur_node.children:
        printRecursive(child, stack)
    stack.pop()

def printTreeNodes(cur_node):
    print(cur_node.char)
    for child in cur_node.children:
        printTreeNodes(child)




def insertRadix(cur_node, word):
    insertRadixRecursive(cur_node, word, 0)

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
                        child.char = child.char[:k+1]
                        split_node.children = child.children
                        split_node.endOfWord = child.endOfWord
                        child.endOfWord = False
                        child.children = []
                        child.children.append(split_node)
                        new_node = node(word[letter+k:])
                        new_node.endOfWord = True
                        child.children.append(new_node)
                        return
                insertRadixRecursive(child, word, letter+k)
                return





if __name__ == "__main__":
    root = node('')
    fd = open("inputText.txt","r")
    for line in range(5):
        word = fd.readline().rstrip()
        print("Inserting Word",word)
        insertText(root, word)
        printTree(root)
    #  printTreeNodes(root)

