import struct

class Float:
    def __init__(self, hex_str):
        self.value = struct.unpack('<f', bytes.fromhex(hex_str))[0]

    def __str__(self):
        return hex(struct.unpack('<I', struct.pack('<f', self.value))[0])

def fma(a, b, c):
    return a * b + c

def main():
    T = int(input())
    for _ in range(T):
        C = Float(input())
        L = int(input())
        LUTs = [[] for _ in range(L)]
        for _ in range(L):
            size, *values = map(lambda x: Float(x), input().split())
            LUTs[-1] = values
        Q = int(input())
        registers = [C]
        for _ in range(Q):
            command = input().split()
            if command[0] == 'L':
                i, j, b = map(int, command[1:])
                mask = (C.value >> j) & ((1 << b) - 1)
                registers.append(LUTs[i][mask])
            elif command[0] == 'N':
                i, j = map(int, command[1:])
                registers.append(Float(hex((~registers[i].value & ~registers[j].value) & 0xffffffff))))
            elif command[0] == 'F':
                i, j, k = map(int, command[1:])
                registers.append(Float(hex(struct.unpack('<I', struct.pack('<f', fma(registers[i].value, registers[j].value, registers[k].value)))[0])))
            elif command[0] == 'C':
                registers.append(Float(command[1]))
        print(registers[-1])

if __name__ == "__main__":
    main()