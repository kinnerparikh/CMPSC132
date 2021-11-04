# HW4
# Due Date: 11/05/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.
#       You might add additional methods to encapsulate and simplify the operations, but they must be
#       thoroughly documented


from typing import no_type_check_decorator


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''
    
    def __init__(self):
        self.root = None
        self.nodesCounter = 0 #remove


    # Modify the insert and _insert methods to allow the operations given in the PDF
    def insert(self, value):
        if self.root is None:
            # creating dictionary pair of lowered and sorted key and value list
            self.root = Node({''.join(sorted(value.lower())): [value]})
            self.nodesCounter += 1 #remove
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        currKey = ''.join(sorted(value.lower()))
        if currKey in node.value:
            node.value[currKey].append(value)
        elif(currKey < list(node.value.keys())[0]):
            if(node.left == None):
                node.left = Node({currKey: [value]})
                self.nodesCounter += 1 #remove
            else:
                self._insert(node.left, value)
        else:   
            if(node.right == None):
                node.right = Node({currKey: [value]})
                self.nodesCounter += 1 #remove
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
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('\\Homeworks\\words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
    '''
    _bst = BinarySearchTree()
    def __init__(self, word_size):
        self.word_size = word_size


    def create(self, file_name):
        # -YOUR CODE STARTS HERE
        # Code for reading the contents of file_name is given in the PDF
        with open(file_name) as f:
            contents = f.read()

        wordCounter = 0 #remove
        for i in contents.split():
            if len(i) <= self.word_size:
                self._bst.insert(i)
                wordCounter += 1 #remove
        
        print(f'Max Length: {self.word_size}, Words Inserted: {wordCounter}, Nodes Inserted: {self._bst.nodesCounter}')

    def getAnagrams(self, word):
        head = self._bst
        key = ''.join(sorted(word.lower()))
        retVal = 'No match'
        while (head != None):
            if (key in head.value):
                retVal = head.value[key]
            elif (key < list(head.value.keys())[0]):
                head = head.left
            else:
                head = head.right
        return retVal
        
ang = Anagrams(9)
ang.create('.\Homeworks\words_large.txt')
'''
if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(BinarySearchTree, globals(), name='HW3',verbose=True)
    
    '''