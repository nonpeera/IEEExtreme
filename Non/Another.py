def solve_queries(nums, queries):
    n = len(nums)
    prefix_sum = [0] * (n + 1)

    # Calculate prefix sum array
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    for query in queries:
        # Find the index where the prefix sum exceeds the query value
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[mid] <= query:
                left = mid + 1
            else:
                right = mid
        
        # Calculate the sum of differences up to the found index
        result = sum(nums[i + 1] - nums[i] for i in range(left - 1))
        print(result)

# Input
n, q = map(int, input().split())
nums = list(map(int, input().split()))
queries = [int(input()) for _ in range(q)]

# Solve the queries
solve_queries(nums, queries)