class Node:
    def __init__(self,value=None) :
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None
    
    def print(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp = temp.next
        print(li)
        return li

def intersection(lla,llb):
    head1 = lla.head
    head2 = llb.head
    if lla.tail !=llb.tail:
        return False
    else:
        while head1 or head2:
            if not head1.next:
                head1 = llb.head
            if not head2.next:
                head2 = lla.head
            if head1 == head2:
                return head1.data
            head1 = head1.next
            head2 = head2.next
llist = LinkedList()
llist.head = Node(10)
second = Node(12)
third = Node(13)
fourth = Node(14)
fifth = Node(12)
sixth = Node(11)
seventh = Node(10)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
llist.tail = seventh
llist.print()


llist2 = LinkedList()
llist2.head = Node(4)
second2 = Node(5)
third2 = Node(3)
llist2.head.next = second2
second2.next = third2
third2.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
llist2.tail = seventh

llist2.print()

print(intersection(llist,llist2))



