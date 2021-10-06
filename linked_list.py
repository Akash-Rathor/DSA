class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedinList:

    def __init__(self):
        self.head = None

    def printList(self):
        x = self.head
        while x:
            print(x.data,end=" , ")
            x=x.next

if __name__ == '__main__':
    a  = linkedinList()
    a.head = Node('First')
    b = Node(3)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    f = Node('End')


    a.head.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    a.printList()


