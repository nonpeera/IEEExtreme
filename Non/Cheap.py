class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.component_count = size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                root_u, root_v = root_v, root_u
            self.parent[root_v] = root_u
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1
            self.component_count -= 1

    def get_component_count(self):
        return self.component_count

def get_connected_components(S, T):
    N = len(S)
    uf = UnionFind(N)
    t_len = len(T)
    
    # สร้าง pattern matching array
    pattern_starts = []
    for i in range(N - t_len + 1):
        if S[i:i + t_len] == T:
            pattern_starts.append(i)
    
    # รวม components ตาม pattern ที่พบ
    for start in pattern_starts:
        for i in range(start, start + t_len - 1):
            uf.union(i, i + 1)
    
    return uf.get_component_count()

def find_minimum_T_length(S, N):
    result = [0] * N
    min_len_for_components = [float('inf')] * (N + 1)
    
    # สร้าง cache สำหรับเก็บ substrings ที่เคยเจอแล้ว
    substring_cache = {}
    
    for t_len in range(1, N + 1):
        # ใช้ set เพื่อเก็บ unique substrings
        seen = set()
        for start in range(N - t_len + 1):
            T = S[start:start + t_len]
            if T in seen:
                continue
            seen.add(T)
            
            # ใช้ cache ถ้าเคยคำนวณแล้ว
            cache_key = (T, t_len)
            if cache_key in substring_cache:
                components = substring_cache[cache_key]
            else:
                components = get_connected_components(S, T)
                substring_cache[cache_key] = components
            
            if components <= N:
                min_len_for_components[components] = min(min_len_for_components[components], t_len)
    
    # ปรับปรุงผลลัพธ์
    min_so_far = float('inf')
    for k in range(N, 0, -1):
        min_so_far = min(min_so_far, min_len_for_components[k])
        result[k - 1] = min_so_far if min_so_far != float('inf') else 0
    
    return result

# Test case
test_input = "aabcabcaa"
N = len(test_input)
result = find_minimum_T_length(test_input, N)
print(" ".join(map(str, result)))  # ควรได้: 9 8 4 6 3 4 2 0 1

# Main program
S = input().strip()
N = len(S)
result = find_minimum_T_length(S, N)
print(" ".join(map(str, result)))