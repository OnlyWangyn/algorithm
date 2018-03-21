class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
    def append(self,node):
        self.next = node
def printlinkList(node):
    while node!=None:
        print node.value
        node=node.next
def printCommonPart(node1,node2):
    while node1!=None and node2!=None:
        if node1.value < node2.value:
            node1=node1.next
        if node1.value>node2.value:
            node2=node2.next
        else:
            print node1.value
            node1=node1.next
            node2=node2.next


node1 = Node(2)
node3 = Node(3)
node1.append(node3)
node5 = Node(5)
node3.append(node5)
node6 = Node(6)
node5.append(node6)
node2 = Node(1)
node2.next=Node(2)
node2.next.next=Node(3)
#printlinkList(node1)
printCommonPart(node1,node2)