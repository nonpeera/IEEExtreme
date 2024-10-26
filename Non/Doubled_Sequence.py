def find_doubled_sequence(n):
    if n == 1:
        return [1, 1]
    if n == 2:
        return None  # No solution exists for N=2
        
    # For n=3 and above, we can construct a solution
    if n >= 3:
        # Initialize the sequence
        sequence = []
        
        # For odd N, we use this pattern
        if n % 2 == 1:
            # First part
            for i in range(1, n + 1):
                sequence.append(i)
            # Second part
            for i in range(2, n):
                sequence.append(i)
            sequence.extend([1, n, n])
            
        # For even N >= 4, we can use this pattern
        else:
            # Build the sequence using a specific pattern that works
            sequence = [2, 3]
            for i in range(2, n-1):
                sequence.append(i+1)
            sequence.append(n)
            sequence.append(3)
            sequence.append(1)
            sequence.append(1)
            sequence.append(n)
            sequence.extend([i+1 for i in range(1, n-1)])
            
        # Verify the solution
        if verify_sequence(sequence, n):
            return sequence
    return None

def verify_sequence(sequence, n):
    if len(sequence) != 2 * n:
        return False
    
    # Check if each number appears exactly twice
    count = {}
    for num in sequence:
        if num not in count:
            count[num] = 0
        count[num] += 1
        if count[num] > 2:
            return False
    
    # Check if each number from 1 to n appears exactly twice
    for i in range(1, n + 1):
        if count.get(i, 0) != 2:
            return False
    
    # Check if Ri - Li = i for each number
    for i in range(1, n + 1):
        left = sequence.index(i)
        right = len(sequence) - 1 - sequence[::-1].index(i)
        if right - left != i:
            return False
            
    return True
output= ""
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = find_doubled_sequence(n)
        if result is None:
            print(-1)
        else:
            print(*result)

if __name__ == "__main__":
    main()