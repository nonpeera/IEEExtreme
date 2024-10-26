def probability_of_alice_winning(R1, B1, R2, B2):
    # Memoization table to store probabilities
    dp = [[[[[None for _ in range(2)] for _ in range(B2 + 1)] for _ in range(R2 + 1)] for _ in range(B1 + 1)] for _ in range(R1 + 1)]

    def compute_probability(r1, b1, r2, b2, turn):
        # Check if the probability is already computed
        if dp[r1][b1][r2][b2][turn] is not None:
            return dp[r1][b1][r2][b2][turn]
        
        # Base cases
        if r1 == 0 or b1 == 0:
            dp[r1][b1][r2][b2][turn] = 0.0  # Alice loses
            return 0.0
        if r2 == 0 or b2 == 0:
            dp[r1][b1][r2][b2][turn] = 1.0  # Alice wins
            return 1.0
        
        if turn == 0:  # Alice's turn as Player A
            # Alice can choose red or blue
            prob_red = r1 / (r1 + b1)
            prob_blue = b1 / (r1 + b1)
            
            # If she chooses red
            guess_red_correct = prob_red * compute_probability(r1 - 1, b1, r2, b2, 1 - turn)
            guess_red_wrong = prob_red * compute_probability(r1, b1, r2 - 1, b2, 1 - turn)
            
            # If she chooses blue
            guess_blue_correct = prob_blue * compute_probability(r1, b1 - 1, r2, b2, 1 - turn)
            guess_blue_wrong = prob_blue * compute_probability(r1, b1, r2, b2 - 1, 1 - turn)
            
            result = (guess_red_correct + guess_red_wrong + guess_blue_correct + guess_blue_wrong) / 2
        
        else:  # Bob's turn as Player A
            # Bob will try to minimize Alice's chance
            prob_red = r2 / (r2 + b2)
            prob_blue = b2 / (r2 + b2)
            
            # If Bob chooses red
            guess_red_correct = prob_red * compute_probability(r1, b1, r2 - 1, b2, 1 - turn)
            guess_red_wrong = prob_red * compute_probability(r1 - 1, b1, r2, b2, 1 - turn)
            
            # If Bob chooses blue
            guess_blue_correct = prob_blue * compute_probability(r1, b1, r2, b2 - 1, 1 - turn)
            guess_blue_wrong = prob_blue * compute_probability(r1, b1 - 1, r2, b2, 1 - turn)
            
            result = (guess_red_correct + guess_red_wrong + guess_blue_correct + guess_blue_wrong) / 2

        # Memoize and return result
        dp[r1][b1][r2][b2][turn] = result
        return result

    # Start the calculation from the initial game state with Alice as Player A (turn = 0)
    return compute_probability(R1, B1, R2, B2, 0)

# Read input
R1, B1, R2, B2 = map(int, input().split())
result = probability_of_alice_winning(R1, B1, R2, B2)

# Print the result with the required precision
print(result)
