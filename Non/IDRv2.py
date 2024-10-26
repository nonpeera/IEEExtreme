from itertools import permutations

def is_valid_sequence(perm):
    n = len(perm)
    mid = (n + 1) // 2
    # ใช้ tuple แทน string เพื่อความเร็ว
    first_half = tuple(sorted(perm[:mid]))
    second_half = tuple(sorted(perm[mid-1:], reverse=True))
    return perm[:mid] == first_half and perm[mid-1:] == second_half

def min_swaps_optimized(source, target):
    # สร้าง position mapping
    pos = {val: idx for idx, val in enumerate(target)}
    visited = [False] * len(source)
    swaps = 0
    
    for start in range(len(source)):
        if visited[start] or source[start] == target[start]:
            continue
            
        cycle_size = 0
        j = start
        
        while not visited[j]:
            visited[j] = True
            j = pos[source[j]]
            cycle_size += 1
            
        swaps += cycle_size - 1
        
    return swaps

def solve(n, mod):
    # สร้าง permutations เป็น tuples แทน strings
    nums = tuple(range(1, n + 1))
    all_perms = list(permutations(nums))
    
    # แยก permutations เป็น valid และ invalid
    valid_perms = []
    invalid_perms = []
    
    # ใช้ set เพื่อเก็บ valid perms ที่ unique
    valid_set = set()
    
    for perm in all_perms:
        if is_valid_sequence(perm):
            if perm not in valid_set:
                valid_perms.append(perm)
                valid_set.add(perm)
        else:
            invalid_perms.append(perm)
    
    if not valid_perms:
        return 0
    
    # คำนวณ min swaps แบบ parallel
    total_swaps = 0
    
    for invalid in invalid_perms:
        min_swaps = float('inf')
        invalid_list = list(invalid)
        
        # หา min swaps กับ valid perm ที่ใกล้ที่สุด
        for valid in valid_perms:
            swaps = min_swaps_optimized(invalid_list, valid)
            min_swaps = min(min_swaps, swaps)
            
        total_swaps = (total_swaps + min_swaps) % mod
    
    return total_swaps

# รับ input และประมวลผล
x, y = map(int, input().split())
result = solve(int(x), int(y))
print(result)