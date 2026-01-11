class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    
    def insertion_at_begin(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    
    def print_list(self):
        itr=self.head
        while itr != None:
            print(itr.data,end=" ")
            itr=itr.next


llist=LinkedList()
llist.insertion_at_begin(10)
llist.insertion_at_begin(20)
llist.insertion_at_begin(30)
llist.print_list()