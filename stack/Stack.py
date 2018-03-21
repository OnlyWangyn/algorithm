class Stack:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size()==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.isEmpty():
            return self.items[self.size()-1]