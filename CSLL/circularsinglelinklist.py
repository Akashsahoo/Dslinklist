class Node:
    def __init__(self,value=None) -> None:
        self.data = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        if self.head:
            tempnode = self.head
            while tempnode :
                yield tempnode
                tempnode = tempnode.next
                if tempnode == self.head:
                    break
                

    def insertion(self,value,location):
        newnode = Node(value=value)
        if not self.head:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        elif location == 0:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = self.head
        elif location == -1:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            tempnode = self.head
            index = 0
            while index < location -1:
                tempnode = tempnode.next
                index += 1

            newnode.next = tempnode.next
            tempnode.next = newnode
    
    def traversal(self):
        if self.head:
            node = self.head
            while node:
               
                print(node.data)
                node = node.next
                if node == self.head:
                    break
    
    def deletion(self,location):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
                self.tail = self.head
            elif location == -1:
                tempnode = self.head
                while tempnode.next != self.tail:
                    tempnode = tempnode.next
                tempnode.next = self.head
                self.tail = tempnode

            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1
                tempnode.next =tempnode.next.next
    
    def entiredeletion(self):
        if self.head:
            self.head = None
            self.tail = None


        

    


circularsinglyLinkedList = CSLL()
circularsinglyLinkedList.insertion(1, -1)
circularsinglyLinkedList.insertion(2, -1)
circularsinglyLinkedList.insertion(3, -1)
circularsinglyLinkedList.insertion(4, -1)
circularsinglyLinkedList.insertion(0, 0)
circularsinglyLinkedList.insertion(0, 4)
circularsinglyLinkedList.traversal()


print([node.data for node in circularsinglyLinkedList]) 

# singlyLinkedList.deletion(0)
# singlyLinkedList.deletion(-1)


#singlyLinkedList.entiredeletion()


print([node.data for node in  circularsinglyLinkedList]) 