def is_inside_rectangle(x, y, rectangle):
    x1, y1, x2, y2 = rectangle
    return x1 < x < x2 and y1 < y < y2

def line_intersection(p1, p2, p3, p4):
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None

    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)

L, N, M = map(int, input().split())
rectangle = (0, 0, L, L)

lines = []
for _ in range(N):
    direction, C = input().split()
    C = float(C)
    if direction == "U":
        lines.append(((0, 0), (C, L)))
    else:
        lines.append(((0, 0), (L, C)))

for _ in range(M):
    direction, C = input().split()
    C = float(C)
    if direction == "U":
        lines.append(((L, 0), (C, L)))
    else:
        lines.append(((L, 0), (0, C)))

intersection_counts = [0] * len(lines)
intersection_points = set()

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if (lines[i][0][0] <= lines[j][1][0] and lines[j][0][0] <= lines[i][1][0] and
            lines[i][0][1] <= lines[j][1][1] and lines[j][0][1] <= lines[i][1][1]):
            
            intersection = line_intersection(lines[i][0], lines[i][1], lines[j][0], lines[j][1])
            if intersection:
                x, y = intersection
                if is_inside_rectangle(x, y, rectangle):
                    if intersection not in intersection_points:
                        intersection_points.add(intersection)
                    intersection_counts[i] += 1
                    intersection_counts[j] += 1

num_edges = len(intersection_counts) + sum(intersection_counts)
print(num_edges - len(intersection_points) + 1)
