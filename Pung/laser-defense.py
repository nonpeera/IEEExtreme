def is_inside_rectangle(point, rectangle):
    x, y = point
    x1, y1, x2, y2 = rectangle
    return x1 < x < x2 and y1 < y < y2

def line_intersection(p1, p2, p3, p4):
    """ 
    Find intersection point of two lines defined by p1-p2 and p3-p4 
    Returns (x, y) of intersection if exists, else None
    """
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return None  # lines are parallel

    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return (x, y)

L, N, M = map(int, input().split())
rectangle = (0, 0, L, L)

n = N+M

lines = []
for i in range(N):
    direction, C = input().split()
    C = float(C)
    if(direction == "U"):
        lines.append(((0, 0), (C, L)))
    else:
        lines.append(((0, 0), (L, C)))
for i in range(M):
    direction, C = input().split()
    C = float(C)
    if(direction == "U"):
        lines.append(((L, 0), (C, L)))
    else:
        lines.append(((L, 0), (0, C)))
        
# สร้างดิกชันนารีเพื่อเก็บจำนวนจุดตัดของแต่ละเส้น
intersection_counts = {i: 0 for i in range(n)}

intersection_points = set()
# หาจุดตัด
for i in range(n):
    for j in range(i + 1, n):
        intersection = line_intersection(lines[i][0], lines[i][1], lines[j][0], lines[j][1])
        if intersection and is_inside_rectangle(intersection, rectangle):
            intersection_counts[i] += 1
            intersection_counts[j] += 1  # เพิ่มนับให้กับเส้นที่สองด้วย
            intersection_points.add(intersection)
# แสดงผลจำนวนจุดตัดของแต่ละเส้น
num_edges = len(intersection_counts)
for line_index, count in intersection_counts.items():
    num_edges += count
print(len(intersection_counts.items()))
print(num_edges-len(intersection_points)+1)