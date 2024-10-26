def max_restaurant_path(sequence):
    n = len(sequence)
    lis = [1] * n  
    
    for i in range(1, n):
        for j in range(0, i):
            if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_restaurant = max(lis)
    
    result_path = []
    current_length = max_restaurant
    for i in range(n - 1, -1, -1):
        if lis[i] == current_length:
            result_path.append(sequence[i])
            current_length -= 1
    result_path.reverse()

    return max_restaurant

test = input("กรุณากรอกลำดับตัวเลขโดยคั่นด้วยช่องว่าง: ")
sequence = list(map(int, test.split()))

max = max_restaurant_path(sequence)

print(max)
