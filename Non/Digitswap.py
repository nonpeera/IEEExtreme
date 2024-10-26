def swap_and_maximize(N, K):
    N = list(str(N))
    max_num = [N[:]]  # To keep track of the maximum number found
    
    def backtrack(current_digits, swaps_left, start):
        if swaps_left == 0:
            current_num = int(''.join(current_digits))
            if current_num > int(''.join(max_num[0])):
                max_num[0] = current_digits[:]
            return
        
        for i in range(start, len(current_digits)):
            for j in range(i + 1, len(current_digits)):
                # Swap digits
                current_digits[i], current_digits[j] = current_digits[j], current_digits[i]
                
                # Check for leading zero
                if current_digits[0] != '0':
                    backtrack(current_digits, swaps_left - 1, i)
                
                # Swap back
                current_digits[i], current_digits[j] = current_digits[j], current_digits[i]
    
    backtrack(N, K, 0)
    
    return int(''.join(max_num[0]))

# Example usage
N, K = map(int, input().split())
result = swap_and_maximize(N, K)
print(result)
