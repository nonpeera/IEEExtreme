from shapely.geometry import LineString, box, Point
from shapely.ops import unary_union


L, N, M = map(int, input().split())

square = box(0, 0, L, L)
print(square)
num_lines = N+M
lines = []
laser_A = []
laser_B = []
# รับพิกัดของเส้น
for i in range(N):
    direction, C = input().split()
    C = float(C)
    if(direction == "U"):
        line = LineString([(0, 0), (C, L)])
        
        # เช็คว่าเส้นอยู่ภายในหรือมีส่วนตัดกับสี่เหลี่ยมไหม
        if square.intersects(line):
            laser_A.append(line.intersection(square))
            lines.append(line.intersection(square))
            
    else:
        line = LineString([(0, 0), (L, C)])
        
        # เช็คว่าเส้นอยู่ภายในหรือมีส่วนตัดกับสี่เหลี่ยมไหม
        if square.intersects(line):
            laser_A.append(line.intersection(square))
            lines.append(line.intersection(square))
            
for i in range(M):
    direction, C = input().split()
    C = float(C)
    if(direction == "U"):
        line = LineString([(L, 0), (C, L)])
        
        # เช็คว่าเส้นอยู่ภายในหรือมีส่วนตัดกับสี่เหลี่ยมไหม
        if square.intersects(line):
            laser_A.append(line.intersection(square))
            lines.append(line.intersection(square))
            
    else:
        line = LineString([(L, 0), (0, C)])
        
        # เช็คว่าเส้นอยู่ภายในหรือมีส่วนตัดกับสี่เหลี่ยมไหม
        if square.intersects(line):
            laser_A.append(line.intersection(square))
            lines.append(line.intersection(square))
    
        



union_lines = unary_union(lines)

# คำนวณจุดตัดและจำนวนเส้นขอบใหม่
vertices = set()
edges_count = 0

for geom in union_lines.geoms:
    if geom.geom_type == 'LineString':
        edges_count += 1
        for coord in geom.coords:
            point = Point(coord)
            # ตรวจสอบว่าจุดไม่อยู่บนขอบของสี่เหลี่ยม
            if 0 < point.x < L and 0 < point.y < L:
                vertices.add((point.x, point.y))

# คำนวณจำนวนช่องตามสูตร V - E + C + 1
regions_count = edges_count - len(vertices) + 1 

# แสดงผลลัพธ์
print(regions_count)

