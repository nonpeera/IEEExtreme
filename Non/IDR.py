def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]):
            for i in range(len(e)+1):
                perms.append(e[:i] + s[-1] + e[i:])
        return perms
def min_swaps_to_target(arr, target):
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        # ทำงานเฉพาะเมื่อ arr[i] ไม่ตรงกับ target[i]
        while arr[i] != target[i]:
            # สลับตัวเลขที่อยู่ติดกันไปข้างหน้าเพื่อให้ได้ลำดับที่ต้องการ
            j = arr.index(target[i])
            # สลับตัวที่อยู่ในตำแหน่ง i และ j
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swaps += 1

    return swaps
unique = []
unswap = []
x ,y = input().split()
xstr= ""
for i in range(1,int(x)+1):
    xstr += str(i)
for i in permutations(xstr):
    s1 = ""
    s2 = ""
    if i[0:(len(i)+1)//2] == s1.join(sorted(i[0:(len(i)+1)//2])) and i[(len(i)+1)//2-1:len(i)] == s2.join(sorted(i[(len(i)+1)//2-1:len(i)])[::-1]):
        unique.append(i)
    else:
        unswap.append(i)

    

ls_compare = []
for i in range(len(unswap)):
    min1 = min_swaps_to_target(list(unswap[i]),list(unique[0]))
    for j in range(1,len(unique)):
       temp = min_swaps_to_target(list(unswap[i]),list(unique[j]))
       if temp < min1:
            min1 = temp
    ls_compare.append(min1)
print(sum(ls_compare)%int(y))