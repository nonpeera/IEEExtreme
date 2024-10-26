def solve():
    N = int(input())
    X_line = list(map(int, input().split()))
    Y_line = list(map(int, input().split()))
    
    A = set(X_line[1:])  # Numbers that must be in first row
    B = set(Y_line[1:])  # Numbers that must be in second row
    MOD = 998244353
    
    # Precompute valid numbers for each row
    all_nums = range(1, 2*N + 1)
    valid_top = [x for x in all_nums if x not in B]
    valid_bottom = [x for x in all_nums if x not in A]
    
    # Sort for faster access
    valid_top.sort()
    valid_bottom.sort()
    
    # Precompute required numbers count
    required_A = len(A)
    required_B = len(B)
    
    # Cache for dynamic programming
    cache = {}
    
    def solve_dp(col, prev_top, prev_bot, used, a_count, b_count):
        if col == N:
            return 1 if a_count == required_A and b_count == required_B else 0
            
        # Check if we can still satisfy A and B requirements
        remaining = N - col
        if a_count + remaining < required_A or b_count + remaining < required_B:
            return 0
            
        state = (col, prev_top, prev_bot, used)
        if state in cache:
            return cache[state]
            
        result = 0
        
        # Binary search for valid starting positions
        top_start = 0
        while top_start < len(valid_top) and valid_top[top_start] <= prev_top:
            top_start += 1
            
        # Try each valid top number
        for i in range(top_start, len(valid_top)):
            top = valid_top[i]
            if used & (1 << top):
                continue
                
            new_a_count = a_count + (top in A)
            if new_a_count > required_A:
                break  # No need to try larger numbers
                
            # Binary search for valid bottom positions
            bot_start = 0
            while bot_start < len(valid_bottom) and (valid_bottom[bot_start] <= prev_bot or valid_bottom[bot_start] <= top):
                bot_start += 1
                
            # Try each valid bottom number
            new_used = used | (1 << top)
            for j in range(bot_start, len(valid_bottom)):
                bottom = valid_bottom[j]
                if bottom <= top or new_used & (1 << bottom):
                    continue
                    
                new_b_count = b_count + (bottom in B)
                if new_b_count > required_B:
                    break  # No need to try larger numbers
                    
                result = (result + solve_dp(
                    col + 1,
                    top,
                    bottom,
                    new_used | (1 << bottom),
                    new_a_count,
                    new_b_count
                )) % MOD
                
        cache[state] = result
        return result
    
    return solve_dp(0, 0, 0, 0, 0, 0)

if __name__ == "__main__":
    print(solve())