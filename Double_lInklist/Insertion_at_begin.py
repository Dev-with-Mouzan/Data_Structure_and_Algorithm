class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList():
    def __init__(self):
        self.head=None

    def inertion_begin(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            self.head.prev=temp
            temp.next=self.head
            self.head=temp

    def print_lst(self):
        itr=self.head
        while itr!=None:
            print(itr.data,end=" ")
            itr=itr.next

    
if __name__ == "__main__":
    dll=DoublyLinkedList()
    dll.inertion_begin(1)
    dll.inertion_begin(2)
    dll.inertion_begin(3)
    dll.print_lst()