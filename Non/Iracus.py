def check_path(S, tree, start, exit_node):
    """
    Simulate Icarus's path through the maze and check if he gets trapped.
    Returns True if he never reaches the exit node, False otherwise.
    """
    current = start
    idx = 0
    visited = set()  # Keep track of visited states (node, index)
    
    while True:
        # Check for already visited state
        if (current, idx) in visited:
            return exit_node not in visited
        
        visited.add((current, idx))
        
        # Get next move from string
        move = S[idx]
        next_node = None
        
        # Move according to the character in S
        if move == 'L':
            next_node = tree[current][0]
        elif move == 'R':
            next_node = tree[current][1]
        elif move == 'U' and current != start:
            # Find parent node
            for node in range(1, len(tree)):
                if tree[node][0] == current or tree[node][1] == current:
                    next_node = node
                    break
        
        # If move is invalid, skip to next character
        if next_node is None:
            idx = (idx + 1) % len(S)
            continue
            
        # If we reach exit node, return False
        if next_node == exit_node:
            return False
            
        current = next_node
        idx = (idx + 1) % len(S)

def solve(S):
    """
    Build a binary tree where Icarus gets trapped and never reaches the exit.
    Returns [N, A, B] and the tree structure, or [-1] if no solution exists.
    """
    max_size = 2 * len(S)
    for N in range(2, max_size + 1):  # From 2 to max_size
        # Loop through possible start and exit nodes
        for start in range(1, N + 1):
            for exit_node in range(1, N + 1):
                if start == exit_node:
                    continue
                    
                # Create a controlled structure, e.g., a binary tree with a certain pattern
                tree = [[0, 0] for _ in range(N + 1)]  # 1-based indexing
                
                # Filling tree with a more structured pattern
                for i in range(1, N + 1):
                    if 2 * i <= N:      # Left child
                        tree[i][0] = 2 * i
                    if 2 * i + 1 <= N:  # Right child
                        tree[i][1] = 2 * i + 1

                # Check if this configuration works
                if check_path(S, tree, start, exit_node):
                    # Format output
                    result = [N, start, exit_node]
                    for i in range(1, N + 1):
                        result.extend(tree[i])
                    return result
    
    return [-1]

def main():
    S = input().strip()
    result = solve(S)
    print(*result)

if __name__ == "__main__":
    main()
