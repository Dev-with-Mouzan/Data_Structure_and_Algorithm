class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    
    def insert_at_end(self,data):
        temp=Node(data)
     
        if self.head != None:
            itr=self.head
            while itr.next != None:
                itr=itr.next
            itr.next=temp
        else:
            self.head=temp
    # print Function
    def print_list(self):
        itr=self.head
        while itr != None:
            print(itr.data,end=" ")
            itr=itr.next
     
     
      
singly_linklist=LinkedList()
singly_linklist.insert_at_end(1)
singly_linklist.insert_at_end(2)
singly_linklist.insert_at_end(3)
singly_linklist.insert_at_end(4)

singly_linklist.print_list()

