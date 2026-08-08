class Stack:
    def __init__(self):
        self.s=[]
    
    def length(self):
        return len(self.s)

    def push(self,value):
        self.s.insert(0,value)

    def pop(self):
        if len(self.s) == 0:
            return "Your stack is empty"
        else:
            return self.s.pop(0)
    
    def peek(self):
        if len(self.s) == 0:
            return "Your stack is empty"
        else:
            return self.s[0]
    


if __name__ == "__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s.length())