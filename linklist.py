
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Linklist :
    def __init__(self):
        self.root = None
    def insert(self,data):
        node = ListNode(data)
        if (self.root == None ):
            self.root = node
            return 
        # print(node.val)
        current = self.root.next
        parent = self.root
        while True:
            if current == None :
                current = node
                parent.next = current
                return 
            else :
                parent = current
                current = current.next



datalist = [1,1,2,3,4,4,5]
link1 = Linklist()
i = 0
while (i<len(datalist)):
    link1.insert(datalist[i])  
    i+=1

node = link1.root
while True :
    if node == None :
        break
    print(node.val)
    node = node.next
    
    