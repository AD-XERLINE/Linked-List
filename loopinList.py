
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
        cur, s = self.head, str(self.head.data)
        while cur.next != None:
            s += "->" + str(cur.next.data)
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

    def index(self, item):
        nowNode = self.head
        N=0
        while(nowNode):
            if nowNode.data == item:

                return N
            nowNode = nowNode.next
            N += 1
        return -1

    def search(self, key):

        current = self.head
        while current is not None:
            if current.data == key:
                return "Found"

            current = current.next

        return "Not Found"
            
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

    def printListform(self):
        temp = self.head
        temp1 = ''
        while (temp):
            temp1 += str(temp.data)
            temp = temp.next
        print("->".join(temp1))

    def Checkloop(self,first,second):
        NowP = self.head
        NowV = self.head
        l = self.head
        t=0
        
        for i in range(first):
            NowP = NowP.next
        # NowP = NowP.prev

        for i in range(second):
            NowV = NowV.next

        NowP.next = NowV
        # print(NowP.next.data)
        print("Set node.next complete!, index:value = "+str(first)+":"+NowP.data+" -> "+str(second)+":"+NowV.data)
        while(l is not None):
            l = l.next
            t += 1
            if t >= self.size():
                # print("Set node.next complete!, index:value = "+str(first)+":"+NowP.data+" -> "+str(second)+":"+NowV.data)
                return True
        if t < self.size():
            return False
        # print(NowP.next.data,NowV.data)

L1 = LinkedList()
inp = list(map(str, input("Enter input : ").split(',')))
Ans = False
for i in inp:
    if i[:1] == "A":
        L1.append(i[2:])
        print(L1.__str__())
    elif i[:1] == "S":

        if L1.isEmpty():
            print("Error! {list is empty}")
        
        elif int(i[2:3]) >= L1.size() :
            print("Error! {index not in length}: "+i[2:3])
            # print("No Loop")
               
        elif int(i[4:]) >= L1.size():
            print("index not in length, append : "+i[4:])
            L1.append(i[4:])
            # print("No Loop")
            # L1.printListform()
        else:

            Ans = L1.Checkloop(int(i[2:3]),int(i[4:]))
            # print(t2)

# ปริ้นการเจอ loop

if L1.isEmpty():
    print("No Loop")
    print("Empty")
elif Ans is True:
    print("Found Loop")
elif Ans is not True:
    print("No Loop")
    print(L1.__str__())
# จัดรูปแบบการบอกลูปว่ามีไหมแล้วการปริ้นค่าทิ้งที่บอกไม่มีลูป