import math

def find_exponent(N):
    # Handle the case where N = 1 (3^0 = 1)
    if N == "1":
        return 0

    # Convert N to a logarithmic base comparison, but avoid direct integer conversion
    # N is extremely large, so treat it as a string and compute log directly
    log_N = math.log10(float(N))
    log_3 = math.log10(3)
    
    # Calculate potential exponent
    z = log_N / log_3

    # Check if z is effectively an integer
    if z.is_integer():
        return int(z)
    else:
        return -1

# Input and output handling
N = input()
print(find_exponent(N))
