def solve_tiles_hit(N, K, elasticities):
    # Create a boolean array to track which tiles are hit
    # Using array instead of set for better performance
    hit = [False] * (N + 1)
    count = 0
    
    # For each ball
    for i in range(K):
        elasticity = elasticities[i]
        # Mark all tiles that will be hit by this ball
        # Starting from elasticity, and moving in multiples
        pos = elasticity
        while pos <= N:
            if not hit[pos]:  # Only count if not already hit
                hit[pos] = True
                count += 1
            pos += elasticity
    
    return count

def main():
    # Read input
    N, K = map(int, input().split())
    elasticities = list(map(int, input().split()))
    
    # Input validation
    assert 1 <= N <= 10**14, "N must be between 1 and 10^14"
    assert 1 <= K <= 100, "K must be between 1 and 100"
    assert len(elasticities) == K, "Must have K elasticities"
    for E in elasticities:
        assert 1 <= E <= 1000, "Each elasticity must be between 1 and 1000"
    
    # Check GCD constraint
    for i in range(K):
        for j in range(i + 1, K):
            assert math.gcd(elasticities[i], elasticities[j]) == 1, "GCD of any two elasticities must be 1"
    
    # Get and print result
    result = solve_tiles_hit(N, K, elasticities)
    print(result)

if __name__ == "__main__":
    import math
    main()


