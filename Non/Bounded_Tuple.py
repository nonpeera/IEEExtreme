def solve_bounded_tuples(N, M, constraints):
    MOD = 998244353
    
    # กรณีไม่มีเงื่อนไข
    if M == 0:
        return "infinity"
    
    # เก็บ constraints ในรูปแบบที่เข้าถึงง่าย
    constraints_by_pos = [[] for _ in range(N)]
    for i, (low, high, K, indices) in enumerate(constraints):
        for pos in indices:
            constraints_by_pos[pos-1].append(i)
    
    # สร้าง dp cache
    max_sum = max(c[1] for c in constraints)
    dp_cache = {}
    
    def dp(pos, prev_sums):
        if pos == N:
            return 1
        
        # ใช้ tuple ของ prev_sums เป็น key เพราะ list ไม่สามารถเป็น key ของ dict ได้
        state = (pos, tuple(prev_sums))
        if state in dp_cache:
            return dp_cache[state]
        
        # หาค่า min และ max ที่เป็นไปได้สำหรับตำแหน่งปัจจุบัน
        min_val = 0
        max_val = max_sum
        
        # ตรวจสอบเงื่อนไขที่เกี่ยวข้องกับตำแหน่งปัจจุบัน
        for constraint_idx in constraints_by_pos[pos]:
            low, high, K, indices = constraints[constraint_idx]
            # คำนวณผลรวมของค่าที่มีอยู่แล้ว
            current_sum = prev_sums[constraint_idx]
            remaining = len([i for i in indices if i-1 >= pos])
            
            if remaining == 1:  # ถ้าเหลือแค่ตำแหน่งปัจจุบัน
                min_val = max(min_val, low - current_sum)
                max_val = min(max_val, high - current_sum)
        
        if min_val > max_val:
            dp_cache[state] = 0
            return 0
            
        count = 0
        # ลองค่าที่เป็นไปได้
        for val in range(min_val, max_val + 1):
            # อัพเดท sums สำหรับทุกเงื่อนไขที่เกี่ยวข้อง
            new_sums = list(prev_sums)
            valid = True
            
            for constraint_idx in constraints_by_pos[pos]:
                low, high, K, indices = constraints[constraint_idx]
                new_sum = new_sums[constraint_idx] + val
                if new_sum > high:
                    valid = False
                    break
                new_sums[constraint_idx] = new_sum
                
            if valid:
                count = (count + dp(pos + 1, new_sums)) % MOD
                
        dp_cache[state] = count
        return count
    
    # สร้าง array เก็บผลรวมเริ่มต้นสำหรับแต่ละเงื่อนไข
    initial_sums = [0] * M
    result = dp(0, initial_sums)
    
    return result if result > 0 else "infinity"

# รับ input
N, M = map(int, input().split())
constraints = []
for _ in range(M):
    low, high, K, *indices = map(int, input().split())
    constraints.append((low, high, K, indices))

# คำนวณและแสดงผล
print(solve_bounded_tuples(N, M, constraints))