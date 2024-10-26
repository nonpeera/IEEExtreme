class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
    
    def __hash__(self):
        return hash((round(self.x, 10), round(self.y, 10)))

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def intersect_line(self, other):
        # Calculate line intersection using parametric form
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = other.p1.x, other.p1.y
        x4, y4 = other.p2.x, other.p2.y
        
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if abs(denominator) < 1e-10:  # Lines are parallel
            return None
            
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        
        if 0 <= t <= 1:
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            return Point(x, y)
        return None
    
    def clip_to_square(self, L):
        # Clip line to square boundaries
        points = []
        # Check intersection with square boundaries
        boundaries = [
            Line(Point(0, 0), Point(L, 0)),  # Bottom
            Line(Point(L, 0), Point(L, L)),  # Right
            Line(Point(L, L), Point(0, L)),  # Top
            Line(Point(0, L), Point(0, 0))   # Left
        ]
        
        for boundary in boundaries:
            intersection = self.intersect_line(boundary)
            if intersection and 0 <= intersection.x <= L and 0 <= intersection.y <= L:
                points.append(intersection)
        
        return points

def main():
    # Read input
    L, N, M = map(int, input().split())
    
    # Store all line segments
    lines = []
    vertices = set()
    
    # Process lines from left side (0, 0)
    for _ in range(N):
        direction, C = input().split()
        C = float(C)
        if direction == "U":
            line = Line(Point(0, 0), Point(C, L))
        else:
            line = Line(Point(0, 0), Point(L, C))
        
        # Clip line to square boundaries
        points = line.clip_to_square(L)
        if len(points) == 2:
            lines.append(Line(points[0], points[1]))
            # Add internal vertices
            for p in points:
                if 0 < p.x < L and 0 < p.y < L:
                    vertices.add(p)
    
    # Process lines from right side (L, 0)
    for _ in range(M):
        direction, C = input().split()
        C = float(C)
        if direction == "U":
            line = Line(Point(L, 0), Point(C, L))
        else:
            line = Line(Point(L, 0), Point(0, C))
        
        # Clip line to square boundaries
        points = line.clip_to_square(L)
        if len(points) == 2:
            lines.append(Line(points[0], points[1]))
            # Add internal vertices
            for p in points:
                if 0 < p.x < L and 0 < p.y < L:
                    vertices.add(p)
    
    # Find all intersection points between lines
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            intersection = lines[i].intersect_line(lines[j])
            if intersection and 0 < intersection.x < L and 0 < intersection.y < L:
                vertices.add(intersection)
    
    # Calculate number of regions using Euler's formula
    # V - E + F = 1, where F is the number of regions
    # E = number of line segments
    # V = number of vertices (intersection points)
    edges_count = len(lines)
    regions_count = edges_count - len(vertices) + 1
    
    print(regions_count)

if __name__ == "__main__":
    main()