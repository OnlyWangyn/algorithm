class Queue:
    def __init__(self,size):
        self.size=size
        self.item=[]
        self.realsize=0
        self.start=0
        self.end=0

    def isEmpty(self):
        return self.realsize==0
    def push(self,value):
        if(self.realsize == self.size):
            print "This queue is full"
            return
        self.realsize+=1
        self.item.append(value)
        self.end=0 if self.end==self.size-1 else self.end+1
    def poll(self):
        if(self.isEmpty()):
            print "This queue is empty"
            return
        self.realsize-=1
        tmp = self.start
        self.start = 0 if self.start==self.size-1 else self.start+1
        return self.item[tmp]
    def peek(self):
        if(self.isEmpty()):
            print "This queue is empty"
            return
        return self.item[self.start]
# qu = Queue(5)
# qu.push(5)
# qu.push(4)
# qu.push(3)
# qu.push(2)
# print qu.poll()
# print qu.poll()
# print qu.poll()
# print qu.poll()