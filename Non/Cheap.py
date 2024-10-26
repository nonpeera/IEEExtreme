class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def min_length_for_components(S):
    N = len(S)
    results = [0] * (N + 1)  # Store minimum length for each k from 1 to N

    # Try each substring length L from 1 to N
    for L in range(1, N + 1):
        union_find = UnionFind(N)
        
        # Connect islands based on the current substring length L
        for i in range(N - L + 1):
            T = S[i:i + L]  # substring of length L
            for j in range(i, i + L - 1):
                union_find.union(j, j + 1)  # Connect consecutive indices

        # Count the number of connected components
        num_components = len(set(union_find.find(x) for x in range(N)))

        # Update the minimum length for the current number of components
        if results[num_components] == 0:
            results[num_components] = L

    # Fill in any missing values with the last known value (or 0 if not possible)
    for k in range(1, N + 1):
        if results[k] == 0:
            results[k] = results[k - 1]

    # Print the result for each k = 1 to N
    print(" ".join(map(str, results[1:])))

# Example usage:
S = "aabcabcaa"
min_length_for_components(S)
