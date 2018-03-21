from Queue import Queue
class Stack:
    def __init__(self,size):
        self.csize = size
        self.stackQueue = Queue(size)
        self.helpQueue = Queue(size)

    def swap(self):
        tempQueue = self.stackQueue
        self.stackQueue = self.helpQueue
        self.helpQueue = tempQueue
    def push(self,value):
        if (self.stackQueue.realsize== self.csize):
            print "This Stack is full"
            return
        self.stackQueue.push(value)
    def poll(self):
        if self.stackQueue.isEmpty():
            print "This Stack is empty"
            return
        while self.stackQueue.realsize!=1:
            self.helpQueue.push(self.stackQueue.poll())
        res = self.stackQueue.poll()
        self.swap()
        return res
    def peek(self):
        if self.stackQueue.isEmpty():
            print "This Stack is empty"
            return
        while self.stackQueue.currentSize()!=1:
            self.helpQueue.push(self.stackQueue.poll())
        res = self.stackQueue.ppll()
        self.helpQueue.push(res)
        self.swap()
        return res
test = Stack(5)
test.push(5)
test.push(4)
test.push(3)
test.push(2)
print test.poll()
