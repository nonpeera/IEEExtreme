from collections import defaultdict

def max_dine(N, stars, roads):
    # Create adjacency list for cities
    adj = defaultdict(list)
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)

    max_dine_count = 0

    def dfs(city, last_dine_stars, visited):
        nonlocal max_dine_count
        dine_count = 0
        # If the city's restaurant has more stars, the critic can dine here
        if stars[city - 1] > last_dine_stars:
            dine_count = 1
            last_dine_stars = stars[city - 1]
        
        # Update max_dine_count
        max_dine_count = max(max_dine_count, dine_count)
        
        for neighbor in adj[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                dine_count += dfs(neighbor, last_dine_stars, visited)
                visited.remove(neighbor)
        
        return dine_count
    
    # Loop through all cities as starting points
    for start in range(1, N + 1):
        visited = set([start])
        dfs(start, -1, visited)
    
    return max_dine_count

# Example usage
N = int(input())  # number of cities
stars = list(map(int, input().split()))  # stars of each restaurant in each city
roads = [tuple(map(int, input().split())) for _ in range(N - 1)]  # roads between cities

# Calculate and print result
result = max_dine(N, stars, roads)
print(result)
