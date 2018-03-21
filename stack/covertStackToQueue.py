from Stack import Stack
class Queue:
    def __init__(self,size):
        self.size = size
        self.queueStack = Stack()
        self.helpStack = Stack()
    def length(self):
        return self.queueStack.size()
    def empty(self):
        return self.queueStack.isEmpty()
    def push(self,value):
        if(self.length() == self.size):
            print "This queue is full"
            return
        self.queueStack.push(value)
    def poll(self):
        if(self.empty() and self.helpStack.isEmpty()):
            print "This queue is empty"
            return
        if(self.helpStack.isEmpty()):
            while not self.empty():
                self.helpStack.push(self.queueStack.pop())
        return self.helpStack.pop()
    def peek(self):
        if(self.empty() and self.helpStack.isEmpty()):
            print "This queue is empty"
            return
        if(self.helpStack.isEmpty()):
            while not self.empty():
                self.helpStack.push(self.queueStack.pop())
        return self.helpStack.peek()
qu = Queue(5)
qu.push(5)
qu.push(4)
qu.push(3)
qu.push(2)
print qu.poll()
print qu.poll()
print qu.poll()
print qu.poll()
