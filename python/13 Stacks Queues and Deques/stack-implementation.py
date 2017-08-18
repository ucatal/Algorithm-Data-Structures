class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())


s.push(1)
s.push('two')

print(s.peek())

s.push(True)
print(s.items)

print(s.pop())
print(s.items)

print(s.size())

print(s.pop())
print(s.pop())
print(s.size())