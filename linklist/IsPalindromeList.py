from stack.Stack import *
class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
def isPalindrome1(node):
    if node==None or node.next==None:
        return True
    sk = Stack()
    head = node
    while head!=None:
        sk.push(head)
        head=head.next
    while sk.peek()!=None:
        if sk.pop().value!=node.value:
            return False
        node=node.next
    return True
def isPalindrome2(node):
    if node==None or node.next==None:
        return True
    sk = Stack()
    head = node
    headfast = node
    while headfast!=None and headfast.next!=None:
        headfast = headfast.next.next
        head=head.next
    while head!=None:
        sk.push(head)
        head=head.next
    while sk.peek()!=None:
        if sk.pop().value!=node.value:
            return False
        node=node.next
    return True
def isPalindrome3(node):
    if node==None or node.next==None:
        return True
    n1 = node
    n2 = node
    while n2!=None and n2.next!=None:
        n2=n2.next.next
        n1=n1.next
    n3=n1.next
    n1.next=None
    while n3!=None:
        tmp = n3.next
        n3.next=n1
        n1=n3
        n3=tmp
    n3 = n1
    n1 = node
    res = True
    while n1!=None and n2!=None:
        if n1.value!=n2.value:
            res=False
            break
        n1=n1.next
        n2=n2.next
    n3next = n3.next
    n3.next = None
    while n3next!=None:
        temp = n3next.next
        n3next.next=n3
        n3= n3next
        n3next = tmp
    return res
node2 = Node(1)
node2.next=Node(2)
node2.next.next=Node(3)
node2.next.next.next=Node(2)
node2.next.next.next.next=Node(1)
print isPalindrome3(node2)