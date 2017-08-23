class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode  = None
def delete_by_index(node, index):
    if not index:
        return node.nextnode
    head = node
    for _ in range(index):
        prev_node, node = node, node.nextnode
    prev_node.nextnode = node.nextnode
    return head


def Delete(head, position):
  
    temp = head
    previous = None
    for i in range(position-1):
        previous = temp
        temp = temp.nextnode
        if temp is None:
            break
    
    if temp is None:
        return
    if temp.nextnode is None:
        return
     
    next = temp.nextnode.nextnode
    temp.nextnode = next
    previous.nextnode =temp    
    
    return previous
    
def printList(head):
    while(head):
        print (" %d " %(head.value)),
        head = head.nextnode

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
j = Node(10)
 
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = g
g.nextnode = h
h.nextnode = i
i.nextnode = j

# result= Delete(a,9)

# printList(result)

res= delete_by_index(a,8)
printList(res)