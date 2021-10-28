class Node:
    def __init__(self, value=-1):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return "%s" % (str(self.value))


def insert(root, value=-1):
    if root is None:
        root = Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
        else:  # don't insert if key already exist in the tree
            pass
    return root


def inorder(root):
    # Inorder (Left, Root, Right)
    if root is not None:
        inorder(root.left)
        print(root)
        inorder(root.right)


def preorder(root):
    # Preorder (Root, Left, Right)
    if root is not None:
        print(root)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    # Postorder (Left, Right, Root)
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root)

def main():
    temp = [47, 5, 3, 70, 23, 53, 15, 66, 81, 64, 85, 31, 83, 33, 9, 7]

    root = None
    for i in temp:
        root = insert(root, i)
    
    postorder(root)

if __name__ == '__main__':
    main()