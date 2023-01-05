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
    
    def nthfromlast(self,m):
        pointer1 = self.head
        pointer2 = self.head
        n = 0 
        while n<m:
            pointer1 = pointer1.next
            n = n +1
        while pointer1:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer2.data
        


if __name__ == "__main__":

	# Creating Empty list
	llist = LinkList()
	llist.head = Node(10)
	second = Node(12)
	third = Node(11)
	fourth = Node(11)
	fifth = Node(12)
	sixth = Node(11)
	seventh = Node(10)

	# Connecting second and third
	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth
	fifth.next = sixth
	sixth.next = seventh

	# Printing data
print("Linked List before removing Duplicates.")
print(llist.print())
# llist.removeDuplicates(llist.head)
print(llist.nthfromlast(2))
print("\nLinked List after removing duplicates.")
print(llist.print())