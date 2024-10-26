from itertools import permutations
N = int(input())
def generate_combinations(required_numbers, additional_numbers):
    # เก็บผลลัพธ์ทั้งหมด
    all_combinations = []
    num_len = N - len(required_numbers)
    # เลือกเลข 2 ตัวจากตัวเลขที่เหลือ
    for extra_numbers in permutations(additional_numbers, num_len):
        # รวมเลขที่ต้องมีและเลขที่เลือกมาได้
        combination = required_numbers + list(extra_numbers)
        # หาความเป็นไปได้ในการจัดเรียงทั้งหมดของชุดตัวเลขนี้
        for perm in permutations(combination):
            # เรียงลำดับจากน้อยไปมาก
            sorted_perm = tuple(sorted(perm))
            if sorted_perm not in all_combinations:  # ตรวจสอบซ้ำ
                all_combinations.append(sorted_perm)

    return all_combinations

def find_matching_combinations(table_1, table_2):
    # เก็บผลลัพธ์ที่ตรงตามเงื่อนไข
    matching_combinations = []

    # ตรวจสอบความเป็นไปได้แต่ละชุด
    for t1 in table_1:
        for t2 in table_2:
            # ตรวจสอบเงื่อนไขแต่ละตำแหน่ง
            if all(t1[i] < t2[i] for i in range(4)) and len(set(t1 + t2)) == 8:
                matching_combinations.append((t1, t2))

    return matching_combinations


X_line = list(map(int, input().split()))
Y_line = list(map(int, input().split()))

A = list(X_line[1:])  # Numbers that must be in first row
B = list(Y_line[1:])  # Numbers that must be in second row

# Precompute valid numbers for each row
all_nums = range(1, 2*N + 1)
valid = [x for x in all_nums if x not in A and x not in B]

# Sort for faster access
valid.sort()

# Precompute required numbers count
required_A = len(A)
required_B = len(B)


# ตัวอย่างการใช้งาน
table_1 = generate_combinations(A, valid)
table_2 = generate_combinations(B, valid)

# หาชุดตัวเลขที่ตรงตามเงื่อนไข
result = find_matching_combinations(table_1, table_2)


print(len(result))