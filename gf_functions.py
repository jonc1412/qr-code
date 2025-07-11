import galois

GF256 = galois.GF(2**8)

# Most common irreducible polynomial of degree 8 (commonly used for QR codes)
irreducible_poly = 0x11D

# Addition and subtraction work the same way in Galois Field arithmetic
def add_sub(a, b):
    # Negative numbers have the same value as positive numbers in Galois Field
    a, b = abs(a), abs(b)

    return a ^ b

exp_table = [0] * 255
# Important to not access log_table[0] as there is no such value a^i == 0 for some integer i
log_table = [-1] * 255

x = 1
for i in range(255):
    exp_table[i] = x
    # log_table is basically the inverse of exp_table
    log_table[x] = i
    # Shifting to get the next power of 2
    x <<= 1
    if x > 255:
        # Need to do polynomial modulo (not integer modulo)
        x ^= 0x11D