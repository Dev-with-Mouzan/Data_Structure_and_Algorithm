class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class Doubly():
    def __init__(self):
        self.head=None

    def inert_end(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            itr=self.head
            while itr.next!=None:
                itr=itr.next
            itr.next=temp
            temp.prev=itr
        
    def pritn_list(self):
        itr=self.head
        while itr!=None:
            print(itr.data,end=" ")
            itr=itr.next
        

if __name__ == "__main__":
    dll=Doubly()
    dll.inert_end(1)
    dll.inert_end(2)
    dll.inert_end(3)
    dll.inert_end(4)
    dll.inert_end(5)
    dll.pritn_list()