class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkList:
    def __init__(self) -> None:
        self.head = None
        
    def print(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp = temp.next
        return li
    
    def removeduplicates(self):
        if self.head:
            hash = set()
            temp = self.head
            hash.add(temp.data)
            while temp.next is not None:
                
                if temp.next.data not in hash:
                    hash.add(temp.next.data)  
                    temp = temp.next 
                else:
                    temp.next = temp.next.next
                    
                
ll = LinkList()
first = Node(1)
second = Node(2)
third = Node(3)
four = Node(3)
five = Node(4)
six = Node(5)
seven = Node(2)

ll.head = first
first.next = second
second.next = third
third.next =four
four.next = five
five.next = six
six.next = seven

print(ll.print())

ll.removeduplicates()
print(ll.print())

                
