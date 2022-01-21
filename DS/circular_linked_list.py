class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None
        
    def add_data(self,data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while(temp.next!=self.head):
                temp =temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    
    def print_it(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data,end = ' -- > ')
                temp = temp.next
                if temp==self.head:
                    break

clist = CircularLinkedList()
clist.add_data(10)
clist.add_data(20)
clist.add_data(30)
clist.add_data(40)
clist.add_data(50)
clist.add_data(60)
clist.print_it()


