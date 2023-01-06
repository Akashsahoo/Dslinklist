class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def printll(self):
        li = []
        temp = self
        while temp:
            li.append(temp.data)
            temp = temp.next
        return li

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
    
    def partition2(self,x):
        curnode = self.head
        smallerhead = None
        smallertail = None
        equalhead = None
        equaltail = None
        greaterhead = None
        greatertail = None
        while curnode:
            nextnode = curnode.next
            curnode.next = None
            if curnode.data<x:
                if not smallerhead:
                    smallerhead = curnode
                    smallertail = curnode
                else:
                    smallertail.next = curnode
                    smallertail = curnode
            
            elif curnode.data==x:
                if not equalhead:
                    equalhead = curnode
                    equaltail = curnode
                else:
                    equaltail.next = curnode
                    equaltail = curnode
            
            elif curnode.data>x:
                if not greaterhead:
                    greaterhead = curnode
                    greatertail = curnode
                else:
                    greatertail.next = curnode
                    greatertail = curnode
            curnode = nextnode
        
        if not smallerhead:
            if not equalhead:
                return greaterhead
            equaltail.next = greaterhead
            return equalhead
        if not equalhead:
            smallertail.next = greaterhead
            return smallerhead
        smallertail.next = equalhead
        equaltail.next = greaterhead
        return smallerhead



        

            




    
    
        


ll = LinkList()
first = Node(1)
second = Node(2)
third = Node(2)
four = Node(1)
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

ll = ll.partition2(2)

print(printll(ll))



            
