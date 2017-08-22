
# double ended queue
# https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Stacks%2C%20Queues%20and%20Deques/Implementation%20of%20Deque.ipynb


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.addFront('hello')
d.addRear('world')

print(d.size())
print(d.removeFront() + ' ' + d.removeRear())

print(d.size())
