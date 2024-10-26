import struct

# Function to handle LUT command
def handle_lut(commands, i, j, b, lut):
    mask = (1 << b) - 1
    index = (commands[i] >> j) & mask
    return lut.get(index, 0)

# Function to handle NAND command
def handle_nand(commands, i, j):
    return ~(int(commands[i]) & int(commands[j])) & 0xFFFFFFFF  # Ensures 32-bit result

# Function to handle FMA command with overflow/underflow checks
def handle_fma_safe(commands, i, j, k):
    a = struct.unpack('!f', struct.pack('!I', commands[i]))[0]
    b = struct.unpack('!f', struct.pack('!I', commands[j]))[0]
    c = struct.unpack('!f', struct.pack('!I', commands[k]))[0]
    result = a * b + c

    # Clamp result to IEEE 754 single-precision float range if out of bounds
    if result > 3.4028235e+38:
        result = float('inf')
    elif result < -3.4028235e+38:
        result = float('-inf')
    elif abs(result) < 1.17549435e-38:
        result = 0.0

    return struct.unpack('!I', struct.pack('!f', result))[0]  # Convert back to 32-bit

# Function to handle Constant command
def handle_constant(h):
    return int(h, 16)

# Core function to execute operations with safe FMA and index bounds checking
def execute_operations_with_safe_fma(test_cases):
    results = []
    
    for case in test_cases:
        c0_hex, lut_definitions, operations = case
        commands = [int(c0_hex, 16)]
        
        # Process LUTs
        lut = {}
        for size, values in lut_definitions:
            for idx, value in enumerate(values):
                lut[idx] = int(value, 16)
        
        # Execute commands with index validation
        for command in operations:
            cmd_type = command[0]
            
            if cmd_type == 'L':
                _, i, j, b = command
                if 0 <= i < len(commands):
                    result = handle_lut(commands, i, j, b, lut)
                    commands.append(result)
                else:
                    commands.append(0)  # Default value if out of bounds
            
            elif cmd_type == 'N':
                _, i, j = command
                if 0 <= i < len(commands) and 0 <= j < len(commands):
                    result = handle_nand(commands, i, j)
                    commands.append(result)
                else:
                    commands.append(0)  # Default value if out of bounds
            
            elif cmd_type == 'F':
                _, i, j, k = command
                if 0 <= i < len(commands) and 0 <= j < len(commands) and 0 <= k < len(commands):
                    result = handle_fma_safe(commands, i, j, k)
                    commands.append(result)
                else:
                    commands.append(0)  # Default value if out of bounds
            
            elif cmd_type == 'C':
                _, h = command
                result = handle_constant(h)
                commands.append(result)
        
        results.append(f'{commands[-1]:08x}')
    
    return results

# Main function with direct input handling
def execute_operations_with_direct_input(data):
    data_lines = data.strip().splitlines()
    T = int(data_lines[0].strip())  # Number of test cases
    idx = 1
    test_cases = []
    
    for _ in range(T):
        try:
            c0_hex = data_lines[idx].strip()
            idx += 1
            
            L = int(data_lines[idx].strip())
            idx += 1
            lut_definitions = []
            
            for __ in range(L):
                k_i = int(data_lines[idx].strip())
                idx += 1
                values = [data_lines[idx + i].strip() for i in range(2 ** k_i)]
                lut_definitions.append((k_i, values))
                idx += 2 ** k_i
            
            Q = int(data_lines[idx].strip())
            idx += 1
            operations = []
            
            for __ in range(Q):
                cmd = data_lines[idx].strip().split()
                if cmd[0] == 'L' and len(cmd) == 4:
                    operations.append(('L', int(cmd[1]), int(cmd[2]), int(cmd[3])))
                elif cmd[0] == 'N' and len(cmd) == 3:
                    operations.append(('N', int(cmd[1]), int(cmd[2])))
                elif cmd[0] == 'F' and len(cmd) == 4:
                    operations.append(('F', int(cmd[1]), int(cmd[2]), int(cmd[3])))
                elif cmd[0] == 'C' and len(cmd) == 2:
                    operations.append(('C', cmd[1]))
                else:
                    raise ValueError("Invalid command format")
                idx += 1
            
            test_cases.append((c0_hex, lut_definitions, operations))
        except Exception as e:
            print(f"Error in parsing test case: {e}")
            return []
    
    results = execute_operations_with_safe_fma(test_cases)
    return results
