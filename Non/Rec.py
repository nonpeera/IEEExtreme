def largest_rectangle_area(heights):
    # Monotonic stack to find max rectangle area
    stack = []
    max_area = 0
    heights.append(0)  # Append sentinel value
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()  # Remove sentinel
    return max_area

def max_rectangle_after_modification(heights, X):
    # Step 1: Calculate max area without any modification
    max_area = largest_rectangle_area(heights[:])

    # Step 2: Try modifying each element to X and calculate max area
    for i in range(len(heights)):
        if heights[i] < X:
            # Modify the height at index i to X temporarily
            original_height = heights[i]
            heights[i] = X
            
            # Calculate area with this modified array
            max_area = max(max_area, largest_rectangle_area(heights))
            
            # Revert the height back
            heights[i] = original_height

    return max_area
# Example usage
N, x = list(map(int, input().split()))
lengths = list(map(int, input().split()))
print(max_rectangle_after_modification(lengths, x))  # Expected output: 15
