class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.head=None
    


    def print_list(self):
        itr=self.head
        while itr != None:
            print(itr.data,end=" ")
            itr=itr.next


if __name__ == "__main__":
    dll=Doubly()
    dll.head=Node(1)
    second=Node(2)
    third=Node(3)
    dll.head.next=second
    second.prev=dll.head
    second.next=third
    third.prev=second
    dll.print_list()