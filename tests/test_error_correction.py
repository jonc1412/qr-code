from qr_code.error_correction import generate_generator_polynomial

def test_generate_generator_polynomial():
    assert generate_generator_polynomial(1, "M") == [1, 251, 67, 46, 61, 118, 70, 64, 94, 32, 45]