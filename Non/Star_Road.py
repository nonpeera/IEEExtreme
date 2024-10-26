
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

N = int(input())
star = [int(x) for x in input().split()]
LsNode = []
for i in range(1,N+1):
    print(i)
    node = Node(i,star[i-1])

for i in range(N):
    a,b = input().split() 
    LsNode[int(a)-1].add_child(LsNode[int(b)-1])
    
for i in LsNode:
    print(i.get_index())
    print(i.get_star())
