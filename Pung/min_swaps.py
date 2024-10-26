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

# ทดสอบด้วย input ที่กำหนด
arr = [1, 2, 3, 4, 8, 9, 7, 6, 5]
target = [1, 2, 3, 4, 9, 8, 7, 6, 5]

# คำนวณจำนวนครั้งที่น้อยที่สุดในการสลับ
min_swaps = min_swaps_to_target(arr, target)
print(min_swaps)
