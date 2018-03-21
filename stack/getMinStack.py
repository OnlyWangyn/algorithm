import Stack
class GetMinStack:
    def __init__(self):
        self.originStack = Stack.Stack()
        self.minValueStack = Stack.Stack()
    def push(self,value):
        if self.originStack.isEmpty():
            self.originStack.push(value)
            self.minValueStack.push(value)
        else:
            current = self.originStack.peek()
            if(value<current):
                self.minValueStack.push(value)
            else:
                self.minValueStack.push(self.minValueStack.peek())
            self.originStack.push(value)
    def pop(self):
        self.originStack.pop()
        self.minValueStack.pop()
    def getMin(self):
        return self.minValueStack.peek()
# s = Stack()

test = GetMinStack()
test.push(4)
test.push(6)
test.push(3)
test.push(2)
test.push(7)
test.push(1)
print test.getMin()
test.pop()
test.pop()
print test.getMin()