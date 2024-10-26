def find_longest_path(graph, stars, N):
    def find_increasing_seq(arr):
        if not arr:
            return 0
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def dfs(node, parent, path):
        nonlocal max_length
        
        # Add current node's star to path
        path.append(stars[node])
        
        # Update max_length with current path
        max_length = max(max_length, find_increasing_seq(path))
        
        # Visit all children
        for next_node in graph[node]:
            if next_node != parent:
                dfs(next_node, node, path)
        
        # Backtrack - remove current node from path
        path.pop()

    max_length = 1
    
    # Try starting from each node
    for start in range(N):
        dfs(start, -1, [])
    
    return max_length

# Input processing
N = int(input())
stars = list(map(int, input().split()))

# Create adjacency list
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(find_longest_path(graph, stars, N))