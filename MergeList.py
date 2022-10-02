
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

    def isEmpty(self):
        return self.head == None

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
        if pos < 0: #ถ้าตำแหน่งที่จะ insert ติดลบให้มันกลายเป็นตัวท้ายงี้เลยคิดว่ามันจะได้
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
    
    def mergeLists(self, list,ID):
        if ID == 1:
            self.head.next = list.head
            return
        list.reverse()
        self.tail.next = list.head
        

L1 = LinkedList()
L2 = LinkedList()
inp = list(map(str, input("Enter Input (L1,L2) : ").split(' ')))

inp[0] = list(inp[0].split('->'))
inp[1] = list(inp[1].split('->'))
ID = 0
for i in range(len(inp[0])):
    L1.append(inp[0][i])
    ID += 1
for i in range(len(inp[1])):
    L2.append(inp[1][i])

print("L1    : "+L1.__str__())
print("L2    : "+L2.__str__())
L1.mergeLists(L2,ID)
print("Merge : "+ L1.__str__())
# print(inp[0])
# print(inp[1])
