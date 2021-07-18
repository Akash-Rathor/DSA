class stack:
    
    def __init__(self):
        self.stack = []

    def _isEmpty(self):
        return self.stack==[]

    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if self._isEmpty():
            return print("error : stack is empty")
        else:
            self.stack.pop()

    def index(self,data):
        try:
            return self.stack.index(data)
        except Exception as e:
            return e,type(e)

s = stack()
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
print(s.stack)



    
