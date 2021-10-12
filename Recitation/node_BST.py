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
    
    def insert(self, value): # Simplified version of insert using a helper method
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:      # This will allow repeated values to be placed in the tree. To avoid this, we do: elif(value>node.value):
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def __delitem__(self, value):
        self._deleteHelper(None, self.root, value)
        return self.printInorder

    def _deleteHelper(self, parent, current, value):
        if current is None:
            return None 
        if current.value > value:
            _____________________________________________ #[1]
        elif current.value < value:
            _____________________________________________ #[2]
        else:
            node_children = self.numChildren(current)
            if node_children == 0 or node_children == 1:
                if current.left is not None:
                    child = ______________________ #[3]
                else:
                    child = ______________________ #[4]
                if (parent is not None) and (parent.left is current):
                    _____________________________________________ #[5]
                elif (parent is not None) and (parent.right is current):
                    _____________________________________________ #[6]
                else:
                    _____________________________________________ #[7]
            else:
                temp = current.right
                parent = current
                while temp.left is not None: 
                    _____________________________________________ #[8]
                    _____________________________________________ #[9]
                current.value = _____________________________________________ #[10]
                self._deleteHelper(______________, _____________, _____________) #[11]

    @property
    def printInorder(self):
        if self.root is None: 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)
    
    def numChildren(self, node_object):
        num = 0
        if node_object.left is not None:
            num += 1
        if node_object.right is not None:
            num += 1
        return num
    
bst_keys = [3, 2, 5, 4, 9, 3.5, 6]
t = BinarySearchTree()
for key in bst_keys:
    t.insert(key)

print(t.numChildren(t.root))              # Displays 2
print(t.numChildren(t.root.left))         # Displays 0
print(t.numChildren(t.root.right))        # Displays 2
print(t.numChildren(t.root.right.right))  # Displays 1