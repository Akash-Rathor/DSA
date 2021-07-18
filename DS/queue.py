class queue:

    def __init__(self):
        self.queue = []

    
    def enqueue(self,data):
        self.queue.append(data)


    def dequeue(self):
        self.queue.pop(0)


    def index(self,data):
        try:
            self.queue.index(data)
        except Exception as e:
            return e


q = queue()

q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.dequeue()

print(q.queue) #-> output - >[6,7,8]