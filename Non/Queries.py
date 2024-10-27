class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index, delta):
        # Increment the index by 1 to convert to 1-based index used by Fenwick Tree
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def sum(self, index):
        # Increment the index by 1 to convert to 1-based index used by Fenwick Tree
        index += 1
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_sum(self, left, right):
        return self.sum(right) - self.sum(left - 1)

import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    
    N = int(data[index])
    Q = int(data[index + 1])
    index += 2
    
    P = list(map(int, data[index:index + N]))
    index += N

    # Adapt P from 1-based to 0-based
    P = [p - 1 for p in P]
    
    # Initialize the Fenwick Tree for range updates
    fenwick_tree = FenwickTree(N)

    output = []

    for _ in range(Q):
        T = int(data[index])
        if T == 0 or T == 1:
            l = int(data[index + 1]) - 1  # Convert to 0-based
            r = int(data[index + 2]) - 1  # Convert to 0-based
            c = int(data[index + 3])
            if T == 0:
                # Update A[l:r] directly by c
                fenwick_tree.add(l, c)  # Add c starting from index l
                fenwick_tree.add(r + 1, -c)  # Subtract c starting from index r + 1 (exclusive)
            else:
                # Update A[P[l]:P[r]] by c
                for i in range(l, r + 1):
                    fenwick_tree.add(P[i], c)  # Use P to update
            index += 4
        else:
            l = int(data[index + 1]) - 1  # Convert to 0-based
            r = int(data[index + 2]) - 1  # Convert to 0-based
            if T == 2:
                # Sum A[l:r]
                total_sum = fenwick_tree.range_sum(l, r)
                output.append(total_sum)
            else:
                # Sum A[P[l]:P[r]]
                total_sum = sum(fenwick_tree.sum(P[i]) for i in range(l, r + 1))
                output.append(total_sum)
            index += 3
            
    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()