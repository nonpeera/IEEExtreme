
class Node:

    def __init__(self,index,star):
        self.index = index
        self.star = star 
        self.child = []
        self.parent = None
    def add_child(self,child):
        self.child.append(child)
    def set_parent(self,parent):
        self.parent = parent
    def get_child (self):
        return self.child
    def get_index (self):
        return self.index
    def get_star (self):
        return self.star


class Stack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      print("Stack is empty")

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      print("Stack is empty")

  def size(self):
    return len(self.items)

  def toList(self):
    return self.items
N = int(input())
star = [int(x) for x in input().split()]
LsNode = []
for i in range(1,N+1):
    node = Node(i,star[i-1])
    LsNode.append(node)

for i in range(N-1):
    a,b = input().split() 
    LsNode[int(a)-1].add_child(LsNode[int(b)-1])
print("------------")
for i in LsNode:
    print(i.get_index(),i.get_star())



