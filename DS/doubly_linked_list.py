class Node:

    def __init__(self,data):
        self.data=data
        self.next = None
        self.pre = None


    
class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def PrintLinkedList(self):
        x = self.head
        while x:
            if x.pre:
                print(x.data,end=' <----> ')
            else:
                print(x.data,end=' --> ')
            
            x = x.next


dlist = DoublyLinkedList()
dlist.head = Node(1)
second = Node(5)
third = Node(9)

dlist.head.next = second
second.pre = dlist.head
second.next = third
third.pre = second

dlist.PrintLinkedList()