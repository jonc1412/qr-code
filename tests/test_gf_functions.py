import galois
from gf_functions import *

GF256 = galois.GF(2**8)

a = 0x56
b = 0x9D

GF_a = GF256(0x56)
GF_b = GF256(0x9D)

def test_add_sub():
    assert add_sub(a, b) == GF_a + GF_b

def test_mult():
    assert mult(a, b) == GF_a * GF_b

def test_div():
    assert div(a, b) == GF_a / GF_b