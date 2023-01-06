class Node:
    def __init__(self,value=None) :
        self.data = value
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,value):
        newnode = Node(value)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    
    def print(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp = temp.next
        print(li)
        return li
           
    def addtwoll(self,ll1,ll2):
        n1 = ll1.head
        n2 = ll2.head
        carry = 0
        while n1 or n2 or carry!=0:
            result = carry
            if n1:
                result += n1.data
                n1 = n1.next
            
            if n2:
                result += n2.data
                n2 = n2.next

            self.add(result%10)
            carry = result // 10

lla = LinkList()
lla.add(1)        
lla.add(7)
lla.add(9)
lla.print()
llb = LinkList()
llb.add(4)        
llb.add(5)
llb.add(6)
llb.print()
llc = LinkList()
llc.addtwoll(lla,llb)
llc.print()