from src import poly_mult

def test_poly_mult():
    assert poly_mult([1, 1], [1, 1, 1]) == [1, 0, 0, 1]
    assert poly_mult([1], [5, 3, 7]) == [5, 3, 7]
    assert poly_mult([1, 1], [1, 1]) == [1, 0, 1]
    assert poly_mult([0], [123, 42, 99]) == [0, 0, 0]