class Queue(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
         self.items.insert(0,item)
        
    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

print(q.isEmpty())
q.enqueue("1")

print(q.size())
q.enqueue("two")
q.enqueue(3)

print(q.deque())
print(q.deque())
print(q.deque()) 