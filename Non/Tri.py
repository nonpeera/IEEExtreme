import math
import heapq

def calculate_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def calculate_stability(triad):
    """Calculate the stability of a triad of points."""
    d1 = calculate_distance(triad[0], triad[1])
    d2 = calculate_distance(triad[1], triad[2])
    d3 = calculate_distance(triad[0], triad[2])
    return max(d1, d2, d3) - min(d1, d2, d3)

def group_points(points):
    """Efficiently group points into triads minimizing the stability."""
    n = len(points)
    indices = list(range(n))
    groups = []
    
    # Sort points based on their coordinates
    sorted_points = sorted((points[i], i) for i in range(n))
    sorted_indices = [idx for _, idx in sorted_points]

    i = 0
    while i < n:
        triad = sorted_indices[i:i+3]
        if len(triad) == 3:
            groups.append(triad)
        i += 3
    
    return groups

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
#12