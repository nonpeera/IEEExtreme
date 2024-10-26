from collections import deque

class Node:
    def __init__(self, index, star):
        self.index = index
        self.star = star
        self.child = []

    def add_child(self, child):
        self.child.append(child)

    def get_child(self):
        return self.child

    def get_star(self):
        return self.star

    def has_child(self):
        return len(self.child) > 0

def max_restaurant_path(sequence):
    n = len(sequence)
    if n == 0:
        return 0
    lis = [1] * n  # Initial lengths of LIS for each position
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

def find_all_paths_bfs(start_node):
    all_paths = []
    queue = deque([(start_node, [start_node.get_star()])])

    while queue:
        current_node, current_path = queue.popleft()
        is_leaf = True

        for child in current_node.get_child():
            if child not in current_path:  # Avoid cycles
                new_path = current_path + [child.get_star()]
                queue.append((child, new_path))
                is_leaf = False

        if is_leaf:
            all_paths.append(current_path)

    return all_paths

def find_max_dining_experience(LsNode):
    max_length = 0
    for start_node in LsNode:
        all_paths = find_all_paths_bfs(start_node)
        for path in all_paths:
            max_res = max_restaurant_path(path)
            max_length = max(max_length, max_res)
    return max_length

# Input and setup graph structure
N = int(input())
stars = list(map(int, input().split()))
LsNode = [Node(i + 1, stars[i]) for i in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    LsNode[a - 1].add_child(LsNode[b - 1])
    LsNode[b - 1].add_child(LsNode[a - 1])

# Calculate and output the maximum length of the optimal path
max_length = find_max_dining_experience(LsNode)
print(max_length)
