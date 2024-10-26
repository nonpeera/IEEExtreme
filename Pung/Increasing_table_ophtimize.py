from itertools import combinations

def generate_combinations(required_numbers, additional_numbers):
    num_len = N - len(required_numbers)

    # สร้างชุดค่าจากหมายเลขเพิ่มเติม
    for extra_numbers in combinations(additional_numbers, num_len):
        # รวมและจัดเรียงตัวเลข
        combination = sorted(required_numbers + list(extra_numbers))
        yield combination  # คืนค่าชุดแต่ละชุดแทนการคืนค่ารายการ

def find_matching_combinations(table_1, table_2):
    matching_combinations = []

    # ตรวจสอบชุดในลักษณะที่ประหยัดหน่วยความจำ
    for t1 in table_1:
        for t2 in table_2:
            # ตรวจสอบเงื่อนไขโดยตรง
            if all(t1[i] < t2[i] for i in range(N)) and len(set(t1 + t2)) == 2 * N:
                matching_combinations.append((t1, t2))

    return matching_combinations

# รับค่าจำนวน N
N = int(input())

# รับค่าตัวเลขที่ต้องการในแถวแรกและแถวที่สอง
X_line = list(map(int, input().split()))
Y_line = list(map(int, input().split()))

A = list(X_line[1:])  # ตัวเลขที่ต้องมีในแถวแรก
B = list(Y_line[1:])  # ตัวเลขที่ต้องมีในแถวที่สอง

# กำหนดหมายเลขที่ถูกต้อง
all_nums = range(1, 2 * N + 1)
valid = [x for x in all_nums if x not in A and x not in B]

# สร้างชุดค่าตารางสำหรับทั้งสองแถว
table_1 = list(generate_combinations(A, valid))
table_2 = list(generate_combinations(B, valid))

# หาชุดค่าที่ตรงตามเงื่อนไข
result = find_matching_combinations(table_1, table_2)

# แสดงผลลัพธ์
print(len(result))
