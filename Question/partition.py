class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def print(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp = temp.next
        return li
    
    def partition(self,x):
        curnode = self.head
        self.tail=self.head
        while curnode:
            nextnode = curnode.next
            curnode.next = None
            if curnode.data<x:
                curnode.next = self.head
                self.head = curnode
            else:
                self.tail.next = curnode
                self.tail = curnode
            curnode = nextnode
        
        if self.tail.next is not None:
            self.tail.next = None

    
    
        


ll = LinkList()
first = Node(1)
second = Node(2)
third = Node(3)
four = Node(14)
five = Node(11)
six = Node(5)
seven = Node(15)


ll.head = first
first.next = second
second.next = third
third.next =four
four.next = five
five.next = six
six.next = seven
ll.tail =  seven

print(ll.print())

ll.partition(6)

print(ll.print())



            
