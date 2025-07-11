from src.encoder import get_version, encode_alphanumeric, encode_data

def test_get_version():
    assert get_version("Alphanumeric", len("HELLO WORLD"), "Q") == 1
    assert get_version("Alphanumeric", len("HELLO THERE WORLD"), "Q") == 2

def test_encode_alphanumeric():
    assert encode_alphanumeric("HELLO WORLD") == '0110000101101111000110100010111001011011100010011010100001101'

def test_encode_data():
    assert encode_data("HELLO WORLD", "Alphanumeric", "M") == "00100000010110110000101101111000110100010111001011011100010011010100001101000000111011000001000111101100000100011110110000010001"