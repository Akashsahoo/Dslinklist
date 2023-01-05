class Node:
    def __init__(self,value=None) -> None:
        self.data = value
        self.prev = None
        self.next = None
        

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        if self.head:
            tempnode = self.head
            while tempnode:
                yield tempnode
                tempnode = tempnode.next

    def insertion(self,value,location):
        newnode = Node(value=value)
        if not self.head:
            self.head = newnode
            self.tail = newnode
            
        elif location == 0:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            self.head.prev = None
        elif location == -1:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
            
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
    
    def forwardtraversal(self):
        if self.head:
            node = self.head
            while node:
                print(node.data)
                node = node.next
    
    def backwardtraversal(self):
        if self.head:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev
    
    def deletion(self,location):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
                self.head.prev = None
            elif location == -1:
                tempnode = self.head
                while tempnode.next != self.tail:
                    tempnode = tempnode.next
                tempnode.next = None
                self.tail = tempnode

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


        

    


doublyLinkedList = DLL()
doublyLinkedList.insertion(1, -1)
doublyLinkedList.insertion(2, -1)
doublyLinkedList.insertion(3, -1)
doublyLinkedList.insertion(4, -1)
doublyLinkedList.insertion(0, 0)
doublyLinkedList.insertion(0, 4)



print([node.data for node in doublyLinkedList]) 

#doublyLinkedList.deletion(0)
# doublyLinkedList.deletion(-1)


#singlyLinkedList.entiredeletion()
doublyLinkedList.forwardtraversal()
doublyLinkedList.backwardtraversal()

# print(reversed([node.data for node in doublyLinkedList]) )