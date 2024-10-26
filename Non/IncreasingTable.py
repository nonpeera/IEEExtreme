def main():
    import sys
    from collections import defaultdict
    
    MOD = 998244353

    N = int(sys.stdin.readline().strip())
    
    if N < 1 or N > 2000:
        print(0)
        return

    A = set()
    B = set()

    for _ in range(2):
        line = list(map(int, sys.stdin.readline().strip().split()))
        count = line[0]
        for number in line[1:count + 1]:
            if _ == 0:
                A.add(number)
            else:
                B.add(number)

    table = create_increasing_table(N)

    find_root_node(table, A, B)

    checked_tables_hashes = set([hash_table(table)])

    current = table

    for i in range(N - 1):
        a = current[0][i + 1]
        b = current[1][i]

        if a in A or b in B:
            continue

        current[0][i + 1] = b
        current[1][i] = a

        table_hash = hash_table(current)

        if table_hash not in checked_tables_hashes:
            checked_tables_hashes.add(table_hash)

    print(len(checked_tables_hashes))


def find_root_node(table, A, B):
    for value in A:
        if value not in table[0]:
            table[0].append(value)
            table[0].sort()
            el_to_remove = find_element_to_remove_for_first_row(table[0], A)
            table[0].remove(el_to_remove)
            table[1].append(el_to_remove)
            table[1].sort()
            table[1].remove(value)

    for value in B:
        if value not in table[1]:
            table[1].append(value)
            table[1].sort()
            el_to_remove = find_element_to_remove_for_second_row(table[1], B)
            table[1].remove(el_to_remove)
            table[0].append(el_to_remove)
            table[0].sort()
            table[0].remove(value)


def find_element_to_remove_for_first_row(row, A):
    for el in reversed(row):
        if not A.__contains__(el):
            return el
    return None


def find_element_to_remove_for_second_row(row, B):
    for el in row:
        if not B.__contains__(el):
            return el
    return None


def create_increasing_table(cols):
    row2 = list(range(1, cols * 2 + 1))
    row1 = row2[:len(row2) // 2]
    return [row1, row2[len(row2) // 2:]]


def hash_table(table):
    return tuple(tuple(row) for row in table)


if __name__ == "__main__":
    main()
