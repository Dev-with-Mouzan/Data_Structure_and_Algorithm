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
            

    def insert_at_specific_place(self,data,number):
        temp=Node(data)
        itr=self.head
        while itr.next!=None:
            if itr.data==number:
                temp.next=itr.next
                itr=temp.next
            itr=itr.next


    
    def print_list(self):
        itr=self.head
        while itr != None:
            print(itr.data,end=" ")
            itr=itr.next
        

llsit=LinkedList()
llsit.insert_at_end(23)
llsit.insert_at_end(45)
llsit.insert_at_specific_place(34,23)
llsit.print_list()

     