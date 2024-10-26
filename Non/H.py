def solve(N, C, R, B):
    MOD = 998244353
    
    # Pre-validate B values
    for i in range(N):
        # ถ้าค่า B[i] ใหญ่เกินไปหรือเล็กเกินไป
        if B[i] > 2*N or B[i] < 1:
            return 0
            
    # Quick validation for known pairs
    for i in range(N):
        a1, a2 = C[2*i], C[2*i+1]
        if a1 != -1 and a2 != -1:
            if R[i] == 0 and min(a1, a2) != B[i]:
                return 0
            if R[i] == 1 and max(a1, a2) != B[i]:
                return 0
    
    # สร้าง bitmask สำหรับตัวเลขที่ใช้แล้ว (เร็วกว่าใช้ array boolean)
    used_mask = 0
    empty_count = 0
    
    # เตรียมข้อมูลที่รู้แล้ว
    for x in C:
        if x != -1:
            used_mask |= (1 << x)
        else:
            empty_count += 1
            
    if empty_count == 0:
        return 1
    
    # สร้าง lookup table สำหรับตัวเลขที่ใช้ได้
    available = []
    for x in range(1, 2*N + 1):
        if not (used_mask & (1 << x)):
            available.append(x)
    
    # ถ้าจำนวนตัวเลขที่เหลือไม่พอกับช่องว่าง
    if len(available) < empty_count:
        return 0
    
    # สร้าง pair constraints
    pair_constraints = []
    for i in range(N):
        a1, a2 = C[2*i], C[2*i+1]
        target = B[i]
        want_min = (R[i] == 0)
        pair_constraints.append((a1, a2, target, want_min))
    
    def can_satisfy_constraint(val1, val2, target, want_min):
        if val1 == -1 or val2 == -1:
            return True
        return (min(val1, val2) == target) if want_min else (max(val1, val2) == target)
    
    def can_potentially_satisfy(val1, val2, target, want_min):
        if val1 == -1 and val2 == -1:
            return True
        if val1 == -1:
            return (val2 >= target) if want_min else (val2 <= target)
        if val2 == -1:
            return (val1 >= target) if want_min else (val1 <= target)
        return can_satisfy_constraint(val1, val2, target, want_min)
    
    # Cache results for positions
    cache = {}
    
    def get_pair_idx(pos):
        return pos // 2
    
    def backtrack(pos, used_mask, prev_valid=True):
        if pos >= 2*N:
            return 1
            
        if not prev_valid:
            return 0
            
        cache_key = (pos, used_mask)
        if cache_key in cache:
            return cache[cache_key]
            
        if C[pos] != -1:
            pair_idx = get_pair_idx(pos)
            if pos % 2 == 1:  # ตำแหน่งที่สองของคู่
                if not can_satisfy_constraint(C[pos-1], C[pos], 
                                           pair_constraints[pair_idx][2], 
                                           pair_constraints[pair_idx][3]):
                    cache[cache_key] = 0
                    return 0
            result = backtrack(pos + 1, used_mask, True)
            cache[cache_key] = result
            return result
        
        total = 0
        pair_idx = get_pair_idx(pos)
        pair_data = pair_constraints[pair_idx]
        
        # ถ้าเป็นตำแหน่งที่สองของคู่ และตำแหน่งแรกถูกเติมแล้ว
        first_of_pair = C[pos-1] if pos % 2 == 1 else pair_data[0]
        
        for num in available:
            if used_mask & (1 << num):
                continue
                
            # Quick validation for pair constraints
            if pos % 2 == 1:
                if not can_satisfy_constraint(first_of_pair, num, 
                                           pair_data[2], pair_data[3]):
                    continue
            elif not can_potentially_satisfy(num, pair_data[1], 
                                          pair_data[2], pair_data[3]):
                continue
                
            new_result = backtrack(pos + 1, used_mask | (1 << num), True)
            total = (total + new_result) % MOD
        
        cache[cache_key] = total
        return total
    
    return backtrack(0, used_mask)

# Input parsing
N = int(input())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
B = list(map(int, input().split()))

# Output
print(solve(N, C, R, B))