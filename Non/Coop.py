from sys import stdin, stdout
from math import gcd
from typing import List, Tuple

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        # Initialize trees with 4*n size to ensure enough space
        self.salary_tree = [0] * (4 * n)
        self.happiness_tree = [0] * (4 * n)
        # Store base values
        self.salaries = [0] * n
        self.happiness = [0] * n
        # Lazy propagation arrays
        self.lazy_set = [(False, 0)] * (4 * n)  # (is_set, value)
        self.lazy_add = [0] * (4 * n)

    def _push_lazy(self, node: int, start: int, end: int) -> None:
        """Propagate lazy updates to children"""
        if start == end:
            return
            
        # Set operation
        if self.lazy_set[node][0]:
            mid = (start + end) // 2
            left_size = mid - start + 1
            right_size = end - mid
            
            # Update children with set value
            self.salary_tree[node*2] = self.lazy_set[node][1] * left_size
            self.salary_tree[node*2+1] = self.lazy_set[node][1] * right_size
            
            # Mark children for lazy propagation
            self.lazy_set[node*2] = self.lazy_set[node]
            self.lazy_set[node*2+1] = self.lazy_set[node]
            self.lazy_add[node*2] = 0
            self.lazy_add[node*2+1] = 0
            
        # Add operation
        if self.lazy_add[node]:
            mid = (start + end) // 2
            left_size = mid - start + 1
            right_size = end - mid
            
            # Update children with add value
            self.salary_tree[node*2] += self.lazy_add[node] * left_size
            self.salary_tree[node*2+1] += self.lazy_add[node] * right_size
            
            # Propagate add value to children
            self.lazy_add[node*2] += self.lazy_add[node]
            self.lazy_add[node*2+1] += self.lazy_add[node]
            
        self.lazy_set[node] = (False, 0)
        self.lazy_add[node] = 0

    def _update_range(self, node: int, start: int, end: int, l: int, r: int, val: int, is_set: bool) -> None:
        """Update range with lazy propagation"""
        if start > r or end < l:
            return
            
        if start >= l and end <= r:
            size = end - start + 1
            if is_set:
                self.salary_tree[node] = val * size
                self.lazy_set[node] = (True, val)
                self.lazy_add[node] = 0
            else:
                self.salary_tree[node] += val * size
                self.lazy_add[node] += val
            return
            
        self._push_lazy(node, start, end)
        mid = (start + end) // 2
        self._update_range(node*2, start, mid, l, r, val, is_set)
        self._update_range(node*2+1, mid+1, end, l, r, val, is_set)
        self.salary_tree[node] = self.salary_tree[node*2] + self.salary_tree[node*2+1]

    def _query_range(self, node: int, start: int, end: int, l: int, r: int) -> int:
        """Query range sum with lazy propagation"""
        if start > r or end < l:
            return 0
            
        if start >= l and end <= r:
            return self.salary_tree[node]
            
        self._push_lazy(node, start, end)
        mid = (start + end) // 2
        return (self._query_range(node*2, start, mid, l, r) +
                self._query_range(node*2+1, mid+1, end, l, r))

    def update_type_0(self, l: int, r: int, c: int) -> None:
        """Set values in range [l,r] to c"""
        # Update segment tree
        self._update_range(1, 0, self.n-1, l, r, c, True)
        
        # Update happiness based on salary changes
        for i in range(l, r+1):
            old_salary = self.salaries[i]
            if old_salary < c:
                self.happiness[i] += 1
            elif old_salary > c:
                self.happiness[i] -= 1
            self.salaries[i] = c

    def update_type_1(self, l: int, r: int, c: int) -> None:
        """Add c to values in range [l,r]"""
        # Update segment tree
        self._update_range(1, 0, self.n-1, l, r, c, False)
        
        # Update happiness based on salary changes
        for i in range(l, r+1):
            self.salaries[i] += c
            if c > 0:
                self.happiness[i] += 1
            elif c < 0:
                self.happiness[i] -= 1

    def query_salary(self, l: int, r: int) -> int:
        """Query sum of salaries in range [l,r]"""
        return self._query_range(1, 0, self.n-1, l, r)

    def query_happiness(self, l: int, r: int) -> int:
        """Query sum of happiness in range [l,r]"""
        return sum(self.happiness[l:r+1])

def reduce_fraction(p: int, q: int) -> str:
    """Reduce fraction to lowest terms"""
    if q < 0:
        p, q = -p, -q
    g = gcd(abs(p), abs(q))
    return f"{p//g}/{q//g}"

def main():
    # Fast input
    n, q = map(int, stdin.readline().split())
    salaries = list(map(int, stdin.readline().split()))
    
    # Initialize segment tree
    seg_tree = SegmentTree(n)
    for i in range(n):
        seg_tree.update_type_0(i, i, salaries[i])
    
    # Process queries
    results = []
    for _ in range(q):
        query = list(map(int, stdin.readline().split()))
        query_type = query[0]
        l, r = query[1] - 1, query[2] - 1  # Convert to 0-based indexing
        
        if query_type <= 1:
            c = query[3]
            if query_type == 0:
                seg_tree.update_type_0(l, r, c)
            else:
                seg_tree.update_type_1(l, r, c)
        else:
            range_len = r - l + 1
            if query_type == 2:
                total = seg_tree.query_salary(l, r)
            else:
                total = seg_tree.query_happiness(l, r)
            results.append(reduce_fraction(total, range_len))
    
    # Fast output
    stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()