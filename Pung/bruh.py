import matplotlib.pyplot as plt

def draw_square_and_lines(size, lines):
    fig, ax = plt.subplots()
    
    # วาดสีเหลี่ยมจัตุรัส
    square = plt.Rectangle((0, 0), size, size, fill=None, edgecolor='blue', linewidth=2)
    ax.add_patch(square)

    # วาดเส้น
    for line in lines:
        ax.plot([line.x1, line.x2], [line.y1, line.y2], color='red', linewidth=2)

    # กำหนดขอบเขตของแกน
    ax.set_xlim(-1, size + 1)
    ax.set_ylim(-1, size + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Square and Lines')
    plt.show()

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

# ตัวอย่างการใช้
size = 20  # ขนาดของสีเหลี่ยมจัตุรัส
lines = [
    Line(0, 0, 10, 20),
    Line(0, 0, 15, 20),
    Line(0, 0, 20, 10),
    Line(20, 0, 0, 15),
    Line(20, 0, 5, 20),
    Line(20, 0, 15, 20),
]

draw_square_and_lines(size, lines)