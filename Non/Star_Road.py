
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



def path(start, destination):
    
  print("Goal State: " + f.value + "\n")
  frontier = Stack()
  frontier.push(start)    # Start with a frontier that contains the initial state.
  currentNode = Node('')
  exploreSet = set()      # Start with an empty explored set.

  foundSolution = False
  while (not frontier.is_empty()):    # If the frontier is empty, then no solution.
    print("Frontier: " + NodeValue(frontier.toList()))
    print("Explore: "+ str(exploreSet))
    print("Current Node: " + currentNode.value + "\n")
    currentNode = frontier.pop() ;    # Remove a node from the frontier
    if(currentNode == destination):   # If node contains goal state, return the solution.
        foundSolution = True
        break
    exploreSet.add(currentNode.value)     # Add the node to the explored set
    for node in currentNode.get_child():  # Expand node
      node.set_parent(currentNode)        # set Parent Node
      if (not node in exploreSet) :       # add resulting nodes to the frontier if they aren't already in the explored set
        frontier.push(node)

  if(foundSolution):
    print("Frontier: " + NodeValue(frontier.toList()))
    print("Explore: " + str(exploreSet))
    print("Current Node: " + currentNode.value)
    path = currentNode.value
    while (not currentNode.parent == None):
      path += " <=== " + currentNode.parent.value+" "
      currentNode = currentNode.parent
    print("Found solution : "+path)
  else:
    print("There is no solution")