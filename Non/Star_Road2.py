from collections import deque
from bisect import bisect_left

class Node:
    def __init__(self, index, star):
        self.index = index
        self.star = star
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def max_restaurant_path_length(node, prev_star):
    # If the star of the current node is not greater than the previous star, return 0
    if node.star <= prev_star:
        return 0
    
    # Initialize max length to 1 (counting the current restaurant)
    max_length = 1

    # Explore each child node
    for child in node.children:
        # Perform DFS on the child and check the path length
        length = max_restaurant_path_length(child, node.star)
        max_length = max(max_length, 1 + length)

    return max_length

def find_max_dining_experience(nodes):
    max_length = 0
    for node in nodes:
        # Start DFS from each node considering no previous star (setting to 0)
        max_length = max(max_length, max_restaurant_path_length(node, 0))
    return max_length

# Input processing
N = int(input())
stars = list(map(int, input().split()))
nodes = [Node(i + 1, stars[i]) for i in range(N)]

# Build the graph
for _ in range(N - 1):
    a, b = map(int, input().split())
    nodes[a - 1].add_child(nodes[b - 1])
    nodes[b - 1].add_child(nodes[a - 1])

# Calculate and output result
max_length = find_max_dining_experience(nodes)
print(max_length)
