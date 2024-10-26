import itertools

def calculate_min_swaps(perm, target):
    n = len(perm)
    swaps = 0
    perm = list(perm)  # Make a mutable copy
    # Count minimum adjacent swaps needed to convert perm to target
    for i in range(n):
        if perm[i] != target[i]:
            # Find the target[i] position in perm
            j = perm.index(target[i], i)
            # Move target[i] to position i using adjacent swaps
            while j > i:
                perm[j], perm[j - 1] = perm[j - 1], perm[j]
                j -= 1
                swaps += 1
    return swaps

def solve(N, M):
    # Create the target pattern
    mid = (N + 1) // 2
    target = list(range(1, mid + 1)) + list(range(N, mid, -1))
    
    total_swaps = 0
    # Generate all permutations of length N
    for perm in itertools.permutations(range(1, N + 1)):
        total_swaps += calculate_min_swaps(perm, target)
        total_swaps %= M  # Keep total within modulo M
    
    return total_swaps

# Read input
N, M = map(int, input().split())

# Calculate and print result
result = solve(N, M)
print(result)
