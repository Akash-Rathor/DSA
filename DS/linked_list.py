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
            print(x.data,end=" --> ")
            x=x.next

    # inserting a node in the first.
    def pushFirst(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # inserting a node after a particular node.
    def pushAfter(self,pre_node,data):
        new_node = Node(data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    # Inserting a node in the end
    def append(self,data):
        new_node = Node(data)
        # check if head exist if not,
        # create new node as a head,
        # otherwise parser the linekd list till the last node and do the operation
        if self.head is None:
            new_node.head = self.head
        else:
            last = self.head
            while last.next:
                last = last.next

        new_node.next = last.next
        last.next = new_node

if __name__ == '__main__':
    a  = linkedinList()
    a.head = Node(1)
    b = Node(2)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    f = Node(7)


    a.head.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print('Printing Linkedin list : ')
    a.printList()
    print('\nPrinting Linkedin list After Inserting at first : ')
    a.pushFirst(0)
    a.printList()
    print('\nPrinting Linkedin list After inserting after a node : ')
    a.pushAfter(b,3)
    a.printList()
    print('\nPrinting Linkedin list After inserting after a node in the end: ')
    a.append(8)
    a.printList()


