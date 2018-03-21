class Node:
    def __init__(self,value):
        self.value = value
        self.next= None
def printLinkList(node):
    while node!=None:
        print node.value
        node=node.next
def smallerequalbigger(node,pivot):
    if node == None or node.next==None:
        return
    nodes=[]
    head = node
    while head!=None:
        nodes.append(head)
        head=head.next
    partiton(nodes,pivot)
    index = 1
    while index < len(nodes):
        nodes[index - 1].next = nodes[index]
        index+=1
    nodes[len(nodes)-1].next=None
    printLinkList(nodes[0])
def partiton(nodes,pivot):
    start = 0
    small = -1
    end = len(nodes)-1
    while start<=end:
        if nodes[start].value > pivot:
            swap(nodes,start,end)
            end-=1
        if nodes[start].value < pivot:
            small+=1
            swap(nodes,small,start)
            start+=1
        if nodes[start].value == pivot:
            start+=1
def smalleuqalbigger2(node,pivot):
    if node == None or node.next==None:
        return
    shead = None
    eHead = None
    bHead = None
    smallNode = None
    equalNode = None
    biggerNode = None
    while node!=None:
        if node.value < pivot:
            if smallNode == None:
                shead=node
                smallNode = node
            else:
                smallNode.next = node
                smallNode = node
        elif node.value == pivot:
            if equalNode == None:
                ehead = node
                equalNode==node
            else:
                equalNode.next = node
                equalNode=node
        else:
            if biggerNode == None:
                bhead=node
                biggerNode == node
            else:
                biggerNode.next = node
                biggerNode=node
    if shead!=None:
        smallNode.next=ehead
        equalNode= smallNode if ehead == None else equalNode
    if equalNode!=None:
        equalNode.next=bhead
    return shead if shead!=None else ehead if ehead!=None else bHead
def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
node = Node(7)
node.next=Node(2)
node.next.next=Node(1)
node.next.next.next=Node(4)
node.next.next.next.next=Node(3)
node.next.next.next.next.next=Node(3)
node.next.next.next.next.next.next=Node(8)
node.next.next.next.next.next.next.next=Node(9)
#smallerequalbigger(node,3)
printLinkList(smallerequalbigger(node,3))

