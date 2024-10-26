
class Node:

  def __init__(self,value):
    self.value = value
    self.child = []
    self.star = 0
    self.parent = None

  def add_child(self,child):
    self.child.append(child)

  def set_parent(self,parent):
    self.parent = parent

  def get_child (self):
    return self.child

N = int(input())
star = [int(x) for x in input().split()]
