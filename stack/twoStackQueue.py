import Stack
class TwoStackQueue:
    def __init__(self):
        self.popStack = Stack.Stack()
        self.pushStack = Stack.Stack()
    def push(self,value):
        self.pushStack.push(value)
    def pop(self):
        if not self.popStack.isEmpty():
            return self.popStack.pop()
        while not self.pushStack.isEmpty():
            self.popStack.push(self.pushStack.pop())
        return self.popStack.pop()
    def peek(self):
        if not self.popStack.isEmpty():
            return self.popStack.peek()
        while not self.pushStack.isEmpty():
            self.popStack.push(self.pushStack.pop())
        return self.popStack.peek()
twoStack = TwoStackQueue()
twoStack.push(1)
twoStack.push(2)
twoStack.push(3)
print twoStack.peek()
print twoStack.peek()
#print twoStack