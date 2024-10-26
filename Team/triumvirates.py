import itertools
import math

def calculate_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_stability(triad):
    """Calculate the stability of a triad of points."""
    d1 = calculate_distance(triad[0], triad[1])
    d2 = calculate_distance(triad[1], triad[2])
    d3 = calculate_distance(triad[0], triad[2])
    return max(d1, d2, d3) - min(d1, d2, d3)

def group_points(points):
    """Group points into triads minimizing the stability."""
    n = len(points)
    indices = list(range(n))
    
    # Generate all possible groupings of points into triads
    min_stability_sum = float('inf')
    best_groups = None
    
    for permutation in itertools.permutations(indices):
        groups = [permutation[i:i+3] for i in range(0, n, 3)]
        stability_sum = sum(calculate_stability([points[g[0]], points[g[1]], points[g[2]]]) for g in groups)
        
        if stability_sum < min_stability_sum:
            min_stability_sum = stability_sum
            best_groups = groups

    return best_groups

def main():
    # Input parsing
    N = int(input().strip())
    points = [tuple(map(int, input().strip().split())) for _ in range(N)]
    # Group points
    groups = group_points(points)
    
    # Output results
    for group in groups:
        print(" ".join(map(str, group)))

if __name__ == "__main__":
    main()
