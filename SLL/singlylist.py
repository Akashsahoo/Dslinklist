class Node:
    def __init__(self,value=None) -> None:
        self.data = value
        self.next = None

class SLL:
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
            newnode.next = self.head
            self.head = newnode
        elif location == -1:
            self.tail.next = newnode
            self.tail = newnode
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
    
    def deletion(self,location):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
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
                tempnode.next =tempnode.next.next
    
    def entiredeletion(self):
        if self.head:
            self.head = None
            self.tail = None


        

    


singlyLinkedList = SLL()
singlyLinkedList.insertion(1, -1)
singlyLinkedList.insertion(2, -1)
singlyLinkedList.insertion(3, -1)
singlyLinkedList.insertion(4, -1)
singlyLinkedList.insertion(0, 0)
singlyLinkedList.insertion(0, 4)
# singlyLinkedList.traversal()


print([node.data for node in singlyLinkedList]) 

# singlyLinkedList.deletion(0)
# singlyLinkedList.deletion(-1)


#singlyLinkedList.entiredeletion()


print([node.data for node in singlyLinkedList]) 