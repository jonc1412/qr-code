from qr_code.poly_functions import poly_mult

def test_poly_mult():
    assert poly_mult([1, 1], [1, 1, 1]) == [1, 0, 0, 1]
    assert poly_mult([1], [5, 3, 7]) == [5, 3, 7]
    assert poly_mult([1, 1], [1, 1]) == [1, 0, 1]
    assert poly_mult([1, 2, 3, 4], [4, 3, 2, 1]) == [4, 11, 20, 30, 20, 11, 4]
    assert poly_mult([0, 1, 0, 1], [1, 0, 1, 0]) == [0, 1, 0, 2, 0, 1, 0]
    assert poly_mult([5, 0, 2], [3, 1, 4]) == [15, 5, 26, 2, 8]
    assert poly_mult([1, -1, 1], [1, 1, 1]) == [1, 0, 1, 0, 1]
    assert poly_mult([2, 0, 1], [0, 3, 0, 4]) == [0, 6, 0, 11, 0, 4]
    assert poly_mult([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [5, 14, 26, 40, 55, 40, 26, 14, 5]
    assert poly_mult([1, 0, 0, 0, 1], [1, 0, 0, 0, 1]) == [1, 0, 0, 0, 2, 0, 0, 0, 1]