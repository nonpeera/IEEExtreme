from shapely.geometry import LineString, box, Point
# รับค่า L, N, M จากบรรทัดแรก
L, N, M = map(int, input("Enter L, N, M: ").split())
square = box(0, 0, L, L)
# รับข้อมูลลำแสงจากเลเซอร์ A
laser_A = []
print("Enter laser A data:")
for _ in range(N):
    direction, C = input().split()
    C = int(C)
    laser_A.append((direction, C))

# รับข้อมูลลำแสงจากเลเซอร์ B
laser_B = []
print("Enter laser B data:")
for _ in range(M):
    direction, C = input().split()
    C = int(C)
    laser_B.append((direction, C))

lines = []
lines.append(laser_A)
lines.append(laser_B)
# แสดงผลเพื่อดูข้อมูลที่รับมา
print("Parking lot size (L):", L)
print("Laser A beams:", laser_A)
print("Laser B beams:", laser_B)
print(lines)
