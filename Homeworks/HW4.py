# HW4
# Due Date: 11/05/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.
#       You might add additional methods to encapsulate and simplify the operations, but they must be
#       thoroughly documented

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Modify the insert and _insert methods to allow the operations given in the PDF
    def insert(self, value):
        if self.root is None:
            # creating dictionary pair of lowered and sorted key and value list
            self.root = Node({''.join(sorted(value.lower())): [value]})
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        # creating key for the value
        currKey = ''.join(sorted(value.lower()))
        if currKey in node.value: # case for anagram
            node.value[currKey].append(value)
        # case for key less than current node (go to left)
        elif(currKey < list(node.value.keys())[0]): 
            if(node.left == None): # empty left side
                node.left = Node({currKey: [value]})
            else:
                self._insert(node.left, value)
        else:   
            if(node.right == None): # empty right side
                node.right = Node({currKey: [value]})
            else:
                self._insert(node.right, value)

    def isEmpty(self):
        return self.root == None

    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)

class Anagrams:
    _bst = BinarySearchTree()
    def __init__(self, word_size):
        self.word_size = word_size

    def create(self, file_name):
        # -YOUR CODE STARTS HERE
        # Code for reading the contents of file_name is given in the PDF
        with open(file_name) as f:
            contents = f.read()

        # running through file
        for i in contents.split():
            if len(i) <= self.word_size:
                self._bst.insert(i)
        
    def getAnagrams(self, word):
        head = self._bst
        key = ''.join(sorted(word.lower()))
        # running through _bst
        while (head != None):
            if (key in head.value): # anagram case
                return head.value[key]
            elif (key < list(head.value.keys())[0]): # key is less than current key
                head = head.left
            else: # key is greater than current key
                head = head.right
        return 'No match'