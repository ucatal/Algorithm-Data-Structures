class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if right_pointer is None:
            LookupError('n is greater than length')
        right_pointer = right_pointer.nextnode

    # return right_pointer
    while right_pointer.nextnode:
        right_pointer=right_pointer.nextnode
        left_pointer=left_pointer.nextnode
    
    return left_pointer
    pass


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)

target_node.value
4



"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)