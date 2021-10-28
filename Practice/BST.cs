namespace BST
{
    class BST
    {
        public class Node
        {
             Node left;
             Node right;
             int val;
            public Node(int val)
            {
                this.val = val;
            }
        }

        Node root;
        public int insert(int value)
        {
            if (root == null)
            {
                root = new Node(value);
                return null;
            }
            return insert(root, new Node(value));
        }

        private int insert(Node current, Node newNode)
        {
            if (current == null)
            {
                current = newNode;
                return null;
            }
            else if(newNode.val < current.val)
            {
                if (current.left != null)
                {
                    return insert(current.left, newNode);
                }
                else
                {
                    current.left = newNode;
                    return null;
                }
            }
            else
            {
                if (current.right != null)
                {
                    return insert(current.right, newNode);
                }
                else
                {
                    current.right = newNode;
                    return null;
                }
            }
        }
    }


}