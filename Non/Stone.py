def optimal_play(R1, B1, R2, B2, is_player_A):
    # Memoization dictionary using tuples as keys
    memo = {}
    
    def solve(R1, B1, R2, B2, is_A_turn, is_A_role):
        if (R1 == 0 and B1 == 0):
            return 1.0 if is_A_role else 0.0
        if (R2 == 0 and B2 == 0):
            return 0.0 if is_A_role else 1.0
            
        state = (R1, B1, R2, B2, is_A_turn, is_A_role)
        if state in memo:
            return memo[state]
            
        # Current player's stones
        curr_R = R1 if is_A_turn else R2
        curr_B = B1 if is_A_turn else B2
        # Other player's stones
        other_R = R2 if is_A_turn else R1
        other_B = B2 if is_A_turn else B1
        
        prob = 0.0
        choices = 0
        
        # Try red stone
        if curr_R > 0:
            choices += 1
            # Probability of opponent guessing red
            if other_R > 0 or other_B > 0:
                next_R1 = R1 - 1 if is_A_turn else R1
                next_R2 = R2 if is_A_turn else R2 - 1
                prob += 0.5 * solve(next_R1, B1, next_R2, B2, not is_A_turn, not is_A_role)
                prob += 0.5 * solve(next_R1, B1, next_R2, B2, not is_A_turn, not is_A_role)
                
        # Try blue stone
        if curr_B > 0:
            choices += 1
            # Probability of opponent guessing blue
            if other_R > 0 or other_B > 0:
                next_B1 = B1 - 1 if is_A_turn else B1
                next_B2 = B2 if is_A_turn else B2 - 1
                prob += 0.5 * solve(R1, next_B1, R2, next_B2, not is_A_turn, not is_A_role)
                prob += 0.5 * solve(R1, next_B1, R2, next_B2, not is_A_turn, not is_A_role)
        
        if choices > 0:
            prob /= choices
            
        memo[state] = prob
        return prob
    
    return solve(R1, B1, R2, B2, True, is_player_A)

# Read input
R1, B1, R2, B2 = map(int, input().split())

# Calculate Alice's winning probability
result = optimal_play(R1, B1, R2, B2, True)
print(f"{result:.9f}")