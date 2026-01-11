class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    
# structure of single linklist has been created 
sinlgle_linklist=LinkedList(34)
print(sinlgle_linklist.head)