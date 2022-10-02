
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizeof = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def reverse(self):
        if(self.head != None):
            prevNode = self.head
            tempNode = self.head
            curNode = self.head.next
            
            prevNode.next = None
            prevNode.prev = None
            
            while(curNode != None):
            
                tempNode = curNode.next
                curNode.next = prevNode
                prevNode.prev = curNode
                prevNode = curNode
                curNode = tempNode

            self.head = prevNode 
            
    def isEmpty(self):
        return self.head == None

    def append(self, item):
        NewNode = Node(item)
        l = self.head
        if (self.head is None):
            self.head = NewNode
            self.sizeof += 1
            return

        while(l.next):
            l = l.next
        l.next = NewNode
        self.tail = NewNode 
        NewNode.prev = l
        self.sizeof += 1

    def addHead(self, item):
        new_node = Node(item)
        if (self.head is None):
            self.head = new_node
            self.sizeof += 1
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
            l = self.head
            while(l.next):
                l = l.next
            self.tail = l
            self.sizeof += 1
        # ใช้ old ไม่ได้เพราะกำหนดใหม่ให้มองเป็นหัวใหม่
        
        
        

    def listprint(self, node):
        while (node is not None):
            print(node.data,end=' '),
            last = node
            node = node.next   

    def insert(self, pos, item):
        t = -1
        l = self.head
        NewNode = Node(item)
        if pos < 0: #ถ้าตำแหน่งที่จะ insert ติดลบให้มันกลายเป็นตัวท้ายงี้เลยคิดว่ามันจะได้ เป็นสมการนี้แหละ
            t = 0
            pos = self.sizeof + pos
            if pos*-1 > self.sizeof:
                self.addHead(item)
                return
            while(t != pos):
                if l is None:
                    l.next = NewNode
                    self.tail = NewNode
                    return
                l = l.next
                t += 1
            l.prev.next = NewNode
            NewNode.next = l
            self.sizeof += 1
            return
            

        if (self.head is None):
            self.head = NewNode
            self.sizeof += 1
            return
        while(t != pos):
            if l.next is None:
                l.next = NewNode
                NewNode.prev = l
                self.tail = NewNode
                self.sizeof += 1
                return
            l = l.next
            t += 1
        
        l.prev.next = NewNode
        NewNode.next = l
        self.sizeof += 1

    def search(self, key):

        current = self.head
        while current is not None:
            if current.data == key:
                return "Found"

            current = current.next

        return "Not Found"

    def index(self, item):
        nowNode = self.head
        N=0
        while(nowNode):
            if nowNode.data == item:
                return N
            nowNode = nowNode.next
            N += 1
        return -1

    def size(self):
        return self.sizeof

    def pop(self, pos):
        if self.head is None:
            return 

        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            self.sizeof -= 1
            return "Success"

        # Find the key to be deleted
        for i in range(pos - 1):
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

L = LinkedList()
inp = input('Enter Input : ').split(',')
# L.append(1)
# L.addHead(2)
# L.append(3)
# L.insert(0,4)
# L.listprint(L.head)
# L.reverse()
# # print(L.search(5))
# L.listprint(L.head)

for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        # ................................................ ถ้าถูกต้องทำช่วง.แต่ถ้าผิดทำหลัง else.
        print(("Success | {1}-> {2}".format(k, before, L)) if k == "Success" else ("Out of Range | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
L.reverse()
print("Linked List Reverse :", L)
