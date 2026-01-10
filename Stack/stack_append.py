class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Your stack is empty"
        else:
            return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            return "Your stack is empty"
        else:
            return self.items[-1]
    
if __name__ == "__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.peek())
  