from bisect import bisect_left

def find_longest_path(graph, stars, N):
    # Optimized LIS calculation using binary search, O(L log L)
    def find_increasing_seq_length(arr):
        if not arr:
            return 0
        lis = []
        for value in arr:
            pos = bisect_left(lis, value)
            # Replace or append value in lis
            if pos < len(lis):
                lis[pos] = value
            else:
                lis.append(value)
        return len(lis)

    def dfs(node, parent, path):
        nonlocal max_length
        
        # Add current node's star to path
        path.append(stars[node])
        
        # Calculate the LIS length for the current path
        max_length = max(max_length, find_increasing_seq_length(path))
        
        # Explore all child nodes
        for next_node in graph[node]:
            if next_node != parent:
                dfs(next_node, node, path)
        
        # Backtrack - remove the current node from path
        path.pop()

    max_length = 1
    
    # Try starting DFS from each node
    for start in range(N):
        dfs(start, -1, [])
    
    return max_length

# Input processing
N = int(input())
stars = list(map(int, input().split()))

# Create adjacency list for the tree
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(find_longest_path(graph, stars, N))
