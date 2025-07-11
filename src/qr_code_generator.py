from encoder import *
from error_correction import *

data = "HELLO WORLD"
error_correction_level = "M"
mode = "Alphanumeric"

qr_code_version = get_version(mode, len(data), error_correction_level)
print(f"QR Code Version: {qr_code_version} | Error Correction Level: {error_correction_level}")
encoded_data = encode_data(data, mode, error_correction_level)
print(f"The encoded data is: {encoded_data}")
codeword_dict = split_codewords(encoded_data, qr_code_version, error_correction_level)
# codeword_dict = split_codewords("0100001101010101010001101000011001010111001001100101010111000010011101110011001000000110000100100000011001100111001001101111011011110110010000100000011101110110100001101111001000000111001001100101011000010110110001101100011110010010000001101011011011100110111101110111011100110010000001110111011010000110010101110010011001010010000001101000011010010111001100100000011101000110111101110111011001010110110000100000011010010111001100101110000011101100000100011110110000010001111011000001000111101100", 5, "Q")
print(codeword_dict)
message_polynomial = generate_message_polynomial(codeword_dict)
print(message_polynomial)
