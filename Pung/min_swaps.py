def min_swaps_to_target_set(arr, targets):
    def count_swaps(arr, target):
        # สร้างสำเนาของ arr เพื่อไม่ให้กระทบต่อ input
        temp_arr = arr[:]
        swaps = 0
        n = len(arr)
        
        for i in range(n):
            while temp_arr[i] != target[i]:
                # สลับตัวเลขเพื่อให้ตรงกับ target[i]
                j = temp_arr.index(target[i])
                temp_arr[j], temp_arr[j - 1] = temp_arr[j - 1], temp_arr[j]
                swaps += 1

        return swaps

    # คำนวณจำนวนการสลับที่น้อยที่สุดสำหรับแต่ละ target ใน targets
    min_swaps = float('inf')
    for target in targets:
        swaps = count_swaps(arr, target)
        min_swaps = min(min_swaps, swaps)

    return min_swaps

# ทดสอบด้วย input ที่กำหนด
arr = [1, 2, 3, 4, 5]
targets = [[1, 2, 5, 4, 3], [1, 3, 5, 4, 2], [1, 4, 5, 3, 2]]

# คำนวณจำนวนครั้งที่น้อยที่สุดในการสลับ
min_swaps = min_swaps_to_target_set(arr, targets)
print("จำนวนครั้งที่น้อยที่สุดในการสลับ:", min_swaps)
