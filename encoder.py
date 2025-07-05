import pandas as pd

# Table contains the corresponding alphanumeric values of the characters
qr_alphanumeric_table = {
    '0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,
    '5': 5,  '6': 6,  '7': 7,  '8': 8,  '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
    'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
    'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
    'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34,
    'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39,
    '+': 40, '-': 41, '.': 42, '/': 43, ':': 44    
}

# Function that generates the binary encoded data of the alphanumeric text
def encode_alphanumeric(text):
    text_len = len(text)
    encoded_data = ""

    # We want each pair of characters
    for i in range(0, text_len, 2):
        # When not the last character
        if i != text_len - 1:
            first_char_val = qr_alphanumeric_table[text[i]]
            second_char_val = qr_alphanumeric_table[text[i+1]]

            # Formula for finding the number representation for each pair of characters
            num_rep = first_char_val * 45 + second_char_val
            bin_rep = bin(num_rep)[2:]

            # Pad the left with 0s to get a 11-bit binary string
            if len(bin_rep) < 11:
                bin_rep = ("0" * (11 - len(bin_rep))) + bin_rep
        # When last character
        else:
            # Last character does not need any special calculations
            num_rep = qr_alphanumeric_table[text[i]]
            bin_rep = bin(num_rep)[2:]

            # Pad the left with 0s to get a 6-bit binary string
            if len(bin_rep) < 6:
                bin_rep = ("0" * (6 - len(bin_rep))) + bin_rep
        
        encoded_data += bin_rep
            
    return encoded_data

def encode_byte(text, err_corr, mode):
    # Getting the DataFrame for the Character Capacity table for alphanumeric values
    # In the future, may expand to include other data types (e.g. numeric, binary, kanji)
    file_path = 'AlphaNumericCharCapacity.csv'
    df = pd.read_csv(file_path)
    df = df.filter(items=['Version', err_corr])

    char_length = len(text)
    
    # Finding the best QR code version for the text based on size
    qr_version = df.loc[df[err_corr] >= char_length, "Version"].iloc[0]

    # The mode indicator for alphanumeric values
    mode_indicator = {"Numeric" : "0001",
                      "Alphanumeric" : "0010",
                      "Byte" : "0100",
                      "Kanji" : "1000",
                      "ECI" : "0111"}
    

    return qr_version

# print(encode_byte("HELLO WORLD", "Q", "Alphanumeric"))