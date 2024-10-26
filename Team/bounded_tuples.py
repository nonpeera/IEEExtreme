MOD = 998244353

def count_valid_assignments(N, M, constraints):
    # If there are no constraints, return "infinity" immediately
    if M == 0:
        return "infinity"

    # Determine the maximum limits for each variable from constraints
    max_values = [min(50, max(high for _, high, _ in constraints)) for _ in range(N)]

    # A recursive function to count valid assignments using backtracking and constraint propagation
    def backtrack(V, index):
        if index == N:  # All values assigned
            if all_constraints_satisfied(V):
                return 1
            return 0
        
        total = 0
        # Iterate over possible values for V[index] up to the calculated max limit for this variable
        for value in range(max_values[index] + 1):
            V[index] = value
            if violates_constraints(V, index):  # Prune if partial assignment violates any constraints
                continue
            total += backtrack(V, index + 1)
            total %= MOD
        
        return total
    
    # Function to check if current values in V satisfy all constraints after all variables are assigned
    def all_constraints_satisfied(V):
        for low, high, indices in constraints:
            subset_sum = sum(V[i - 1] for i in indices)
            if subset_sum < low or subset_sum > high:
                return False
        return True
    
    # Pruning function to check constraint violation for the current partial assignment
    def violates_constraints(V, up_to_index):
        for low, high, indices in constraints:
            subset_sum = sum(V[i - 1] for i in indices if i - 1 <= up_to_index)
            # Check if subset_sum is outside the valid range based on assigned values so far
            if subset_sum > high:
                return True
        return False
    
    # Check if any constraint allows for an infinite solution
    for low, high, indices in constraints:
        if high >= 1e18:
            return "infinity"
    
    # Initialize V with 0s and start backtracking
    V = [0] * N
    result = backtrack(V, 0)
    return result

# Input Parsing
def parse_input():
    N, M = map(int, input().split())
    constraints = []
    for _ in range(M):
        line = list(map(int, input().split()))
        low, high, K = line[0], line[1], line[2]
        indices = line[3:]  # remaining values are indices
        constraints.append((low, high, indices))
    return N, M, constraints

# Main execution
if __name__ == "__main__":
    # Parse the input
    N, M, constraints = parse_input()
    # Compute the result
    result = count_valid_assignments(N, M, constraints)
    # Print the result
    print(result)
