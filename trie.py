class node:
    def __init__(self, chr):
        self.char = chr
        self.children = []


def find(node, pattern):
    for letter in pattern:
        tamanho = len(node.children)
        if tamanho == 0:
            print("Not Found ", pattern)
            return
        for i in range(tamanho):
            if letter == node.children[i].char:
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
    for letter in word:
        tamanho = len(cur_node.children)
        if tamanho == 0:
            new_node = node(letter)
            cur_node.children.append(new_node)
            cur_node = new_node
            print("Inserted letter ",letter)
        else:
            for i in range(tamanho):
                if letter == cur_node.children[i].char:
                    cur_node = cur_node.children[i]
                    break
                else:
                    if i == tamanho-1:
                        new_node = node(letter)
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
        return 0
    for j in range(len(cur_node.children)):
        if cur_node.children[j].char == word[i]:
            if(removeRecursive(cur_node.children[j], word, i+1)):
                del cur_node.children[j]
                if len(cur_node.children) == 0:
                    return 1
                else:
                    return 0
            else:
                return 0
    return 0


def printTree(root_node):
    stack = []
    for child in root_node.children:
        printRecursive(child, stack)

def printRecursive(cur_node, stack):
    stack.append(cur_node.char)
    if(len(cur_node.children) == 0):
        print("".join(stack))
        stack.pop()
        return
    for child in cur_node.children:
        printRecursive(child, stack)
    stack.pop()



if __name__ == "__main__":
    root = node('')
    insert(root, "gone")
    find(root, "go")
    find(root, "gonewild")
    fd = open("inputText.txt","r")
    lines = fd.readlines()
    print(lines[0])
    for line in lines[0:2]:
        print(line)
        insertText(root, line)
    printTree(root)
    remove(root, "gone")
    printTree(root)

