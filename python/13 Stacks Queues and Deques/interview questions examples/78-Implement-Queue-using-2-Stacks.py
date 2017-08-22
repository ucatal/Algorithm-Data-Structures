class Queue2Stacks(object):
    def __init__(self):
        self.innerStack = []
        self.outerStack = []

    def enqueue(self, item):
        self.innerStack.append(item)

    def dequeue(self):
        if not self.outerStack:
            while self.innerStack:
                self.outerStack.append(self.innerStack.pop())

        return self.outerStack.pop()


"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())
