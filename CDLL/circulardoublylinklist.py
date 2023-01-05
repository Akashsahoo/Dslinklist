class Node:
    def __init__(self,value=None) -> None:
        self.data = value
        self.prev = None
        self.next = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        if self.head:
            tempnode = self.head
            while tempnode:
                yield tempnode
                print(tempnode.data)
                tempnode = tempnode.next
                if tempnode == self.head:
                    break
    
    def insertion(self,value,location):
        newnode = Node(value=value)
        if not self.head:
            self.head = newnode
            self.head.prev = self.tail
            self.tail = newnode
            self.tail.next = self.head
            
        elif location == 0:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            self.head.prev = self.tail
            self.tail.next = self.head
        elif location == -1:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head
            self.head.prev = self.tail
            
        else:
            tempnode = self.head
            index = 0
            while index < location -1:
                tempnode = tempnode.next
                index += 1
            tempnode.next.prev = newnode
            newnode.prev = tempnode
            newnode.next = tempnode.next
            tempnode.next = newnode
    
    def deletion(self,location):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif location == -1:
                tempnode = self.head
                while tempnode.next != self.tail:
                    tempnode = tempnode.next
                tempnode.next = self.head
                self.tail = tempnode
                self.head.prev = self.tail

            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next.next
                nextnode.prev = tempnode
                tempnode.next = nextnode
    
    def entiredeletion(self):
        if self.head:
            self.head = None
            self.tail = None
    
    def forwardtraversal(self):
        if self.head:
            node = self.head
            while node:
                print(node.data)
                node = node.next
                if node == self.head:
                    break

    def backwardtraversal(self):
        if self.head:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev
                if node == self.tail:
                    break
    

circulardoublyLinkedList = CDLL()
circulardoublyLinkedList.insertion(1, -1)
circulardoublyLinkedList.insertion(2, -1)
circulardoublyLinkedList.insertion(3, -1)
circulardoublyLinkedList.insertion(4, -1)
circulardoublyLinkedList.insertion(0, 0)
circulardoublyLinkedList.insertion(0, 4)



print([node.data for node in circulardoublyLinkedList]) 
circulardoublyLinkedList.deletion(0)
circulardoublyLinkedList.deletion(-1)


circulardoublyLinkedList.entiredeletion()
circulardoublyLinkedList.forwardtraversal()
circulardoublyLinkedList.backwardtraversal()

# print(reversed([node.data for node in circulardoublyLinkedList]) )