import numpy as np

def solve_puzzle(grid_size, commands):
    # สร้างตาราง
    grid = np.zeros(grid_size)

    # กำหนดตำแหน่งเริ่มต้น (สมมติว่าเริ่มที่มุมซ้ายล่าง)
    row, col = grid_size[0] - 1, 0

    for command in commands:
        if command == 'U':
            row -= 1
        elif command == 'D':
            row += 1
        elif command == 'L':
            col -= 1
        elif command == 'R':
            col += 1

        # ตรวจสอบขอบเขต
        if row < 0 or row >= grid_size[0] or col < 0 or col >= grid_size[1]:
            print("Out of bounds")
            return

    return grid[row, col]

# ตัวอย่างการใช้งาน
grid_size = (30, 30)
commands = ['U', '10', 'U', '25', 'R', '10', 'L', '15', 'U', '20']
result = solve_puzzle(grid_size, commands)
print(result)