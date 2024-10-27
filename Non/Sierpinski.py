# Function to determine the color based on bitwise AND
def find_color(x, y):
    # If there's no overlap in bits, the point is red (1), else blue (0)
    return 1 if (x & y) == 0 else 0

# Input and query handling
Q = int(input().strip())
results = []
for _ in range(Q):
    x, y = map(int, input().strip().split())
    results.append(find_color(x, y))

# Output results
for result in results:
    print(result)
