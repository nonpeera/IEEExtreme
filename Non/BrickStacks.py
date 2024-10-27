import bisect

def arrange_bricks(N, x, lengths):
    # Step 1: Sort the lengths of the bricks in ascending order
    lengths.sort()
    
    # Step 2: List to hold the top brick of each stack
    tops = []
    stacks = []

    # Step 3: Go through each brick
    for length in lengths:
        # Use binary search to find the leftmost stack whose top brick + x <= current brick
        pos = bisect.bisect_left(tops, length - x)
        
        if pos < len(tops):  # If we found a suitable stack
            stacks[pos].append(length)  # Place brick on this stack
            tops[pos] = length  # Update the top of this stack
        else:
            # If no suitable stack, create a new stack
            stacks.append([length])
            tops.append(length)

    # Step 4: Print the results in the required format
    print(len(stacks))  # Number of stacks
    for stack in stacks:
        print(len(stack), ' '.join(map(str, reversed(stack))))  # Number of bricks and the bricks in the stack in descending order

# Input reading
N, x = map(int, input().split())
lengths = list(map(int, input().split()))
arrange_bricks(N, x, lengths)
