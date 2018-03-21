class Node:
    def __init__(self,value):
        self.value =value
        self.next=None
        self.rand = None
def printlinkList(node):
    while node!=None:
        print node.value
        if(node.rand!=None):
            print node.rand.value
        node=node.next
def copyListWithRandom(node):
    if node == None or node.next == None:
        return
    head = node
    while head!=None:
        cloneNode = Node(head.value)
        cloneNode.next = head.next
        head.next = cloneNode
        if(head.next == None):
            break
        head = head.next.next
    head = node
    while head!=None:
        head.next.rand = head.rand
        if(head.next == None):
            break
        head=head.next.next
    head1 = node.next
    result = head1
    head = node
    while head!=None:
        head.next = head1.next
        if(head1.next==None):
            break
        head1.next = head1.next.next
        head = head.next
        head1= head1.next
    printlinkList(node)
    print "======================="
    printlinkList(result)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

node1.rand = node3
node2.rand = None
node4.rand = node2
node3.rand = node1

copyListWithRandom(node1)
