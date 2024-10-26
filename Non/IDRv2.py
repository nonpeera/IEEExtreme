def get_permutations(n):
    from itertools import permutations
    return [''.join(p) for p in permutations(''.join(str(i) for i in range(1, n+1)))]

def is_valid_sequence(seq):
    mid = (len(seq) + 1) // 2
    first_half = seq[:mid]
    second_half = seq[mid-1:]
    return (
        ''.join(sorted(first_half)) == first_half and
        ''.join(sorted(second_half, reverse=True)) == second_half
    )

def min_swaps(arr1, arr2):
    # สร้าง position mapping
    pos = {val: idx for idx, val in enumerate(arr2)}
    visited = [False] * len(arr1)
    swaps = 0
    
    for i in range(len(arr1)):
        if visited[i] or pos[arr1[i]] == i:
            continue
            
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = pos[arr1[j]]
            cycle_size += 1
            
        swaps += cycle_size - 1
    
    return swaps

def solve(x, y):
    # สร้าง permutations ทั้งหมด
    all_perms = get_permutations(x)
    
    # แยก permutations ที่ถูกต้องและไม่ถูกต้อง
    valid_perms = []
    invalid_perms = []
    
    for perm in all_perms:
        if is_valid_sequence(perm):
            valid_perms.append(perm)
        else:
            invalid_perms.append(perm)

    # คำนวณ minimum swaps
    total_swaps = 0
    for invalid in invalid_perms:
        min_swaps_needed = float('inf')
        invalid_list = list(invalid)
        
        for valid in valid_perms:
            valid_list = list(valid)
            swaps = min_swaps(invalid_list, valid_list)
            min_swaps_needed = min(min_swaps_needed, swaps)
            
        total_swaps += min_swaps_needed
        
    return total_swaps % y

# รับ input และแสดงผล
x, y = map(int, input().split())
print(solve(x, y))