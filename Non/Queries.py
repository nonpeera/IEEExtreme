def update_array(arr, P, l, r, c, type):
    if type == 0:
        for i in range(l, r+1):
            arr[i] += c
    elif type == 1:
        for i in range(l, r+1):
            arr[P[i]] += c

def query_sum(arr, P, l, r, type):
    if type == 2:
        total = 0
        for i in range(l, r+1):
            total += arr[i]
        return total
    elif type == 3:
        total = 0
        for i in range(l, r+1):
            total += arr[P[i]]
        return total

# Read input
N, Q = map(int, input().split())
P = list(map(int, input().split()))
arr = [0] * N

for _ in range(Q):
    query_type, l, r, c = map(int, input().split())
    if query_type < 2:
        update_array(arr, P, l, r, c, query_type)
    else:
        print(query_sum(arr, P, l, r, query_type))