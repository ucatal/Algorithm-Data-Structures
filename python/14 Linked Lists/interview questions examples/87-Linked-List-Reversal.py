class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def reverse(head):
    current  = head
    previous = None
    nextnode = None
    
    while current:        
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer ot the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous = current
        current = nextnode

    return previous

    pass

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

# 2
# 3
# 4

reverse(a)


print( d.nextnode.value)
print( c.nextnode.value)
print( b.nextnode.value)

# 3
# 2
# 1