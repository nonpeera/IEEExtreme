from collections import defaultdict
from bisect import bisect_left

class Node:
    def __init__(self, index, star):
        self.index = index
        self.star = star
        self.adj = []  # Changed to adjacency list for cleaner code
    
    def add_edge(self, node):
        self.adj.append(node)

def find_longest_increasing_subsequence(sequence):
    if not sequence:
        return 0
    
    tails = [float('inf')] * len(sequence)
    tails[0] = sequence[0]
    length = 1
    
    for num in sequence[1:]:
        if num > tails[length - 1]:
            tails[length] = num
            length += 1
        else:
            pos = bisect_left(tails, num, 0, length)
            tails[pos] = num
    
    return length

def find_max_dining_experience(nodes):
    N = len(nodes)
    # dp[node][parent] stores the maximum LIS length for the subtree rooted at node
    dp = defaultdict(lambda: defaultdict(lambda: -1))
    # paths[node][parent] stores the best path for the subtree
    paths = defaultdict(lambda: defaultdict(list))
    
    def dfs(node_idx, parent_idx, visited):
        if dp[node_idx][parent_idx] != -1:
            return dp[node_idx][parent_idx], paths[node_idx][parent_idx]
        
        current_node = nodes[node_idx]
        max_length = 1  # Minimum LIS length is 1 (the node itself)
        best_path = [current_node.star]
        
        # Try all possible paths through children
        for next_node in current_node.adj:
            next_idx = next_node.index - 1
            if next_idx != parent_idx and next_idx not in visited:
                visited.add(next_idx)
                sub_length, sub_path = dfs(next_idx, node_idx, visited)
                visited.remove(next_idx)
                
                # Try including current node with the subpath
                test_path = [current_node.star] + sub_path
                current_length = find_longest_increasing_subsequence(test_path)
                
                if current_length > max_length:
                    max_length = current_length
                    best_path = test_path
        
        dp[node_idx][parent_idx] = max_length
        paths[node_idx][parent_idx] = best_path
        return max_length, best_path
    
    # Try starting from each node
    global_max = 0
    for start in range(N):
        visited = {start}
        length, _ = dfs(start, -1, visited)
        global_max = max(global_max, length)
    
    return global_max

def main():
    # Input processing
    N = int(input())
    stars = list(map(int, input().split()))
    
    # Create nodes
    nodes = [Node(i + 1, stars[i]) for i in range(N)]
    
    # Build the graph
    for _ in range(N - 1):
        a, b = map(int, input().split())
        nodes[a - 1].add_edge(nodes[b - 1])
        nodes[b - 1].add_edge(nodes[a - 1])
    
    # Calculate and output result
    result = find_max_dining_experience(nodes)
    print(result)

if __name__ == "__main__":
    main()