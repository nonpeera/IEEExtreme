def max_subarray_sum(arr):
    max_ending = max_total = arr[0]
    for i in range(1, len(arr)):
        max_ending = max(arr[i], max_ending + arr[i])
        max_total = max(max_total, max_ending)
    return max_total

def solve_test_case():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # For each pair, determine if flipping would help
    # A flip helps if it makes the numbers more positive in a way that improves
    # the maximum subarray sum
    for i in range(0, n-1, 2):
        # Current values
        a, b = arr[i], arr[i+1]
        # Flipped values
        flip_a, flip_b = -a, -b
        
        # Look at the maximum possible sum ending at position i-1
        prefix_sum = 0
        prefix_max = 0
        if i > 0:
            curr_sum = 0
            for j in range(i):
                curr_sum = max(arr[j], curr_sum + arr[j])
                prefix_sum = curr_sum
                prefix_max = max(prefix_max, curr_sum)
        
        # Look at the maximum possible sum starting at position i+2
        suffix_max = 0
        if i+2 < n:
            curr_sum = 0
            for j in range(n-1, i+1, -1):
                curr_sum = max(arr[j], curr_sum + arr[j])
                suffix_max = max(suffix_max, curr_sum)
        
        # Decide whether to flip based on which combination gives better overall sum
        sum_without_flip = max(prefix_max, # prefix only
                             suffix_max,    # suffix only
                             prefix_sum + a + b + suffix_max, # full sequence
                             a + b,         # just the pair
                             prefix_sum + a + b, # prefix + pair
                             a + b + suffix_max) # pair + suffix
                             
        sum_with_flip = max(prefix_max, # prefix only
                           suffix_max,   # suffix only
                           prefix_sum + flip_a + flip_b + suffix_max, # full sequence
                           flip_a + flip_b,        # just the flipped pair
                           prefix_sum + flip_a + flip_b, # prefix + flipped pair
                           flip_a + flip_b + suffix_max) # flipped pair + suffix
        
        if sum_with_flip > sum_without_flip:
            arr[i], arr[i+1] = flip_a, flip_b
    
    return max_subarray_sum(arr)

def main():
    t = int(input())
    for _ in range(t):
        print(solve_test_case())

if __name__ == "__main__":
    main()