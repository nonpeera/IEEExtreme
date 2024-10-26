def arrange_bricks(N, x, lengths):
    # Step 1: Sort the lengths of the bricks
    lengths.sort()
    
    # Step 2: List to hold stacks
    stacks = []

    # Step 3: Go through each brick
    for length in lengths:
        # Binary search to find the right stack to place the current brick
        low, high = 0, len(stacks)
        while low < high:
            mid = (low + high) // 2
            if stacks[mid][-1] + x <= length:
                high = mid  # Look for a lower stack
            else:
                low = mid + 1  # Look for a higher stack
        
        # If we found a valid stack to place the brick
        if low < len(stacks):
            stacks[low].append(length)
        else:
            stacks.append([length])  # Start a new stack with the current brick
    
    # Step 4: Print the results
    print(len(stacks))  # Number of stacks
    for stack in stacks:
        print(len(stack), ' '.join(map(str, reversed(stack))))  # Print the stack from biggest to smallest

# Input reading
N, x = list(map(int, input().split()))
lengths = list(map(int, input().split()))
arrange_bricks(N, x, lengths)