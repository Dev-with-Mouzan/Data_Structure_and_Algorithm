class circular_Queue:
    def __init__(self,size):
        self.items=[None]*size
        self.size=size
        self.front=self.rear=-1

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,value):
        if (self.rear+1)%self.size==self.front:
            print("Queue is full")
        elif self.front==-1:
            self.front=self.rear=0
            self.items.insert(self.rear,value)
        else:
            self.rear=(self.rear+1)%self.size
            self.items.insert(self.rear,value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        elif self.front==self.rear:
            temp=self.items[self.front]
            self.front=self.rear=-1
            return temp
        
        else:
            print(self.items[self.front])
            self.front=(self.front+1)%self.size
        

if __name__=="__main__":
    q=circular_Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    