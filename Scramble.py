
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sizeof = 0

    def __clear__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data)
        while cur.next != None:
            s += " " + str(cur.next.data)
            cur = cur.next
        return s

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
        self.sizeof += 1

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            self.sizeof += 1
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
        self.tail = new_node
        self.sizeof += 1

    def pophead(self, pos):
        if self.head is None:
            return 
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            self.sizeof -= 1
            return 
        
    def size(self):
        # print(self.sizeof)
        return self.sizeof

    def bootomup(self,p):
        T = LinkedList()
        l = self.head
        t = 0
        while(t<p):
            T.insertAtEnd(l.data)
            l = l.next
            t+=1
        self.head = l
        self.tail.next = T.head

    def Riffle(self,p):
        T = LinkedList()
        R = LinkedList()
        l = self.head
        t = 0
        if p == 1:
            return self.__str__()

        while(t<p):
            T.insertAtEnd(l.data)
            l = l.next
            self.pophead(0)
            t+=1
        # print(l.data)
        # print(self.__str__())
        while(l and not T.isEmpty()):
            R.insertAtEnd(T.head.data)
            T.pophead(0)
            R.insertAtEnd(self.head.data)
            self.pophead(0)
            l = l.next
        if not T.isEmpty():
            # print(T.sizeof)
            for i in range(T.sizeof):
                R.insertAtEnd(T.head.data)
                T.pophead(0)
        if not self.isEmpty():
            for i in range(self.sizeof):
                R.insertAtEnd(self.head.data)
                self.pophead(0)
            
        return R.__str__()

def createLL(LL):
    L = LinkedList()
    for i in range(len(LL)):
        L.insertAtEnd(LL[i])
    return L
    # print(L.__str__())

def printLL(head):
    return head.__str__()

def SIZE(head):
    return head.size()

def scarmble(head, b, r, size):
    backbottomup = printLL(head)
    Pros = (size *b)//100
    head.bootomup(Pros)
    print("BottomUp {0:.3f} % : {1}".format(b,printLL(head)))
    backriffle = printLL(head)
    Pros = (size *r)//100
    print("Riffle {0:.3f} % : ".format(r)+head.Riffle(Pros))
    print("Deriffle {0:.3f} % : {1}".format(r,backriffle))
    print("Debottomup {0:.3f} % : {1}".format(b,backbottomup))
    print("",end='')

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)

# scarmble(h, 30, 60, SIZE(h))
for i in inp2.split('|'):
    h = createLL(inp1.split())
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h)) #<-------------------
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h)) #<-------------------
    print('-' * 50)
