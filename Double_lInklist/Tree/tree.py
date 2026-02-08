class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def preorder(root):
    if root!=None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)

    print("Preorder Traversal:")
    preorder(root)

    print("\nInorder Traversal:")
    inorder(root)

    print("\nPostorder Traversal:")
    postorder(root)