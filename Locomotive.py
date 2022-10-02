
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __clear__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

    def printListBefore(self):
        temp = self.head
        temp1 = ""
        while (temp):
            # print(str(temp.data) + " <- ", end="")
            temp1 += str(temp.data)
            temp = temp.next
        print("Before :"," <- ".join(temp1))
    
    def printListAfter(self):
        temp = self.head
        temp1 = ""
        while (temp):
            # print(str(temp.data) + " <- ", end="")
            temp1 += str(temp.data)
            temp = temp.next
        print("After :"," <- ".join(temp1))

    def senddata(self,linkedlist):
        linkedlist = self.head
        temp1 = ""
        while (linkedlist):
            # print(str(temp.data) + " <- ", end="")
            temp1 += str(linkedlist.data)
            linkedlist = linkedlist.next
        return temp1

print(" *** Locomotive ***")
lst = input("Enter Input : ").split(' ')
llist = LinkedList()
llist1 = LinkedList()
llist2 = LinkedList()
for i in range(len(lst)):
    llist.insertAtEnd(lst[i])
llist.printListBefore()

for i in range(len(lst)):
    if lst[i] != "0":
        llist1.insertAtEnd(lst[i])
    elif lst[i] == "0":
        llist2.insertAtEnd((llist1.senddata(llist1)))
        llist1.__clear__()
        # ให้ดูตัวtemp กลายเป็น None 
llist2.insertAtBeginning(llist1.senddata(llist1))
llist2.insertAtBeginning(0)
# llist2.insertAtBeginning(llist1)
# llist2.insertAtBeginning(0)
llist2.printListAfter()
# llist.insertAtEnd(1)
# llist.insertAtBeginning(2)
# llist.insertAtBeginning(3)
# llist.insertAtEnd(4)
# llist.insertAfter(llist.head.next, 5)
