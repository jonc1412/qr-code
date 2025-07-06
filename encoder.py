import pandas as pd
from constants import ALPHANUMERIC_CAPACITY, ALPHANUMERIC_TABLE, MODE_INDICATOR, ERROR_CORRECTION, CHAR_COUNT_INDICATOR_BITS

# Function that generates the binary encoded data of the alphanumeric text
def encode_alphanumeric(text):
    text_len = len(text)
    encoded_data = ""

    # We want each pair of characters
    for i in range(0, text_len, 2):
        # When not the last character
        if i != text_len - 1:
            first_char_val = ALPHANUMERIC_TABLE[text[i]]
            second_char_val = ALPHANUMERIC_TABLE[text[i+1]]

            # Formula for finding the number representation for each pair of characters
            num_rep = first_char_val * 45 + second_char_val
            bin_rep = bin(num_rep)[2:]

            # Pad the left with 0s to get a 11-bit binary string
            if len(bin_rep) < 11:
                bin_rep = bin_rep.zfill(11)
        # When last character
        else:
            # Last character does not need any special calculations
            num_rep = ALPHANUMERIC_TABLE[text[i]]
            bin_rep = bin(num_rep)[2:]

            # Pad the left with 0s to get a 6-bit binary string
            if len(bin_rep) < 6:
                bin_rep = bin_rep.zfill(6)
        
        encoded_data += bin_rep
            
    return encoded_data

def encode_byte(text, err_corr, mode):
    char_length = len(text)
    
    # Hard coded for Alphanumeric values, NEED TO FIX LATER
    for version, values in ALPHANUMERIC_CAPACITY.items():
        if char_length <= values[err_corr]:
            qr_version = version
            break
    
    # First 4 bits of the encoded data
    if mode == "Alphanumeric":
        mode_indicator = MODE_INDICATOR[mode]
        encoded_text = mode_indicator

    # Finding the # of bits required to encode the character length of the text
    for version, bit_count in CHAR_COUNT_INDICATOR_BITS[mode].items():
        if qr_version <= version:
            char_count_bit_len = bit_count
            break

    encoded_text += bin(char_length)[2:].zfill(char_count_bit_len)
    encoded_text += encode_alphanumeric(text)

    # Adding terminator bits as necessary
    # Finding the total number of data bits that are required for this QR code version & error correction level
    total_bits = ERROR_CORRECTION[qr_version][err_corr] * 8
    if total_bits - len(encoded_text) < 4:
        encoded_text += "0" * (total_bits - len(encoded_text))
    else:
        encoded_text += "0" * 4

    # Addding pad bytes if the length of the encoded_text is not a multiple of 8
    encoded_text += "0" * (8 - (len(encoded_text) % 8))

    # Adding pad bytes if the length of the encoded_text does not fill max capacity
    # 11101100 00010001 is the specific set of bytes that must be added as pad bytes
    qr_code_req_bits = ERROR_CORRECTION[qr_version][err_corr] * 8
    for i in range((qr_code_req_bits - len(encoded_text)) // 8):
        if i % 2 == 0:
            encoded_text += "11101100"
        else:
            encoded_text += "00010001"

    return encoded_text

print(encode_byte("HELLO WORLD", "Q", "Alphanumeric"))