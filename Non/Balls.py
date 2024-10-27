import math
from itertools import combinations

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def count_hit_tiles(N, elasticities):
    unique_tiles = 0
    K = len(elasticities)
    
    # Iterate over combinations of elasticities of size 1 to 5 for inclusion-exclusion
    for r in range(1, min(K, 5) + 1):
        for combo in combinations(elasticities, r):
            # Calculate LCM of the current combination
            current_lcm = combo[0]
            for e in combo[1:]:
                current_lcm = lcm(current_lcm, e)
                # If LCM exceeds N, break early
                if current_lcm > N:
                    break
            
            # If LCM is within bounds, apply inclusion-exclusion
            if current_lcm <= N:
                hit_count = N // current_lcm
                if r % 2 == 1:
                    unique_tiles += hit_count  # Add for odd size of combination
                else:
                    unique_tiles -= hit_count  # Subtract for even size of combination

    return unique_tiles

N, K = map(int, input().split())
elasticities = list(map(int, input().split()))
print(count_hit_tiles(N, elasticities))  # Output should be 12
