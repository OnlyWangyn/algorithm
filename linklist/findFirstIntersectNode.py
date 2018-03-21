#encoding=utf-8
#两个概念，相交点和入环点
class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
def getFirstIntersectNode(head1,head2):
    if head1==None or head2==None:
        return None
    loop1 = findLoopNode(head1)
    loop2 = findLoopNode(head2)
    if(loop1==None and loop2==None):
        return noLoop(head1,head2,None)
    if loop1!=None and loop2!=None:
        return bothLoop(head1,head2,loop1,loop2)
    return None
def noLoop(head1,head2,end):
    count = 0
    curr1=head1
    curr2 = head2
    while curr1!=end:
        count+=1
        curr1=curr1.next
    while curr2!=end:
        count-=1
        curr2=curr2.next
    cur1 = head1 if count>0 else head2
    cur2 = head2 if count>0 else head1
    count = abs(count)
    while count>0:
        cur1=cur1.next
        count-=1
    while cur1!=cur2:
        cur1=cur1.next
        cur2=cur2.next
    return cur1
def bothLoop(head1,head2,loop1,loop2):
    if(loop1==loop2):
        return noLoop(head1,head2,loop1)
    else:
        cur = loop1.next
        while cur!=loop1:
            if cur == loop2:
                return cur
            cur=cur.next
        return None
def findLoopNode(node):
    if node.next == None or node.next.next == None:
        return None
    fast = node.next.next
    slow = node.next
    while fast!=slow:
        if fast.next==None or fast.next.next == None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = node
    while fast!=slow:
        fast = fast.next
        slow=slow.next
    return fast
#test case1 俩个无环的链表相交
head1 = Node(1);
head1.next = Node(2);
head1.next.next =Node(3);
head1.next.next.next = Node(4);
head1.next.next.next.next = Node(5);
head1.next.next.next.next.next =Node(6);
head1.next.next.next.next.next.next = Node(7);

head2 =Node(0);
head2.next =Node(9);
head2.next.next = Node(8);
head2.next.next.next = head1.next.next.next.next.next;
print getFirstIntersectNode(head1,head2).value

#test case2　两个有环的链表相交，并且环互相重合
head1 =Node(1);
head1.next = Node(2);
head1.next.next =Node(3);
head1.next.next.next = Node(4);
head1.next.next.next.next = Node(5);
head1.next.next.next.next.next =Node(6);
head1.next.next.next.next.next.next =  Node(7);
head1.next.next.next.next.next.next = head1.next.next.next; # 7->4

# 0->9->8->2...
head2 =  Node(0);
head2.next = Node(9);
head2.next.next = Node(8);
head2.next.next.next = head1.next; # 8->2
print getFirstIntersectNode(head1, head2).value


#0->9->8->6->4->5->6..
head2 = Node(0);
head2.next = Node(9);
head2.next.next = Node(8);
head2.next.next.next = head1.next.next.next.next.next; # 8->6
print getFirstIntersectNode(head1, head2).value
#test case3 两个有环的链表相交，并且环互相重合相交的点不重合，可以任意返回一个
