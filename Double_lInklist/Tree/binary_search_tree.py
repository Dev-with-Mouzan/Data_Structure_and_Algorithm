# Node for tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Search Tree

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print("Inorder traversal of the binary search tree is:")
    inorder(root)

    key = 100
    if search(root, key):
        print(f"\n{key} found in the binary search tree.")
    else:
        print(f"\n{key} not found in the binary search tree.")