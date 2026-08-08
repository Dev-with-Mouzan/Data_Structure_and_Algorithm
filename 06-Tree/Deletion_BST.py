class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def minValueNode(node):
    current=node
    while(current.left!=None):
        current=current.left
    return current

def delete(root,key):
    if root == None:
        return root
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if root.left == None:
            temp=root.right
            root=None
            return temp
        elif root.right == None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root

def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if data<root.data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
    return root

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


if __name__=="__main__": 
    root=Node(50)
    root=insert(root,30)
    insert(root,20)
    insert(root,40)
    insert(root,70)
    insert(root,60)
    insert(root,80)

    print("Inorder traversal of the binary search tree is:")
    inorder(root)

    key=70
    root=delete(root,key)

    print("\nInorder traversal of the binary search tree is:")
    inorder(root)