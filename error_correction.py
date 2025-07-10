from constants import ERROR_CORRECTION
from encoder import encode_data

def split_codewords(data, qr_version , err_corr):
    num_blocks_group1 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["num_blocks_group1"]
    num_codewords_group1 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["data_codewords_group1"]
    num_blocks_group2 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["num_blocks_group2"]
    num_codewords_group2 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["data_codewords_group2"]

    print(f'Number of blocks in group 1: {num_blocks_group1} with {num_codewords_group1} codewords')
    print(f'Number of blocks in group 2: {num_blocks_group2} with {num_codewords_group2} codewords')
    print(f'The total number of codeword blocks: {num_blocks_group1 * num_codewords_group1 + num_blocks_group2 * num_codewords_group2}\n\n')

    group1_dict = dict()

    codeword_start_index = 0
    codeword_final_index = 8

    for i in range(1, num_blocks_group1+1):
        group1_dict[i] = dict()

        for j in range(0, num_codewords_group1):
            current_codeword = data[codeword_start_index:codeword_final_index]
            group1_dict[i][j] = current_codeword

            codeword_start_index += 8
            codeword_final_index += 8
        
    print(group1_dict)

    if num_blocks_group2 > 0:
        group2_dict = dict()


        for i in range(1, num_blocks_group2+1):
            group2_dict[i] = []
            
            for j in range(0, num_codewords_group2):
                current_codeword = data[codeword_start_index:codeword_final_index]
                group2_dict[i][j] = current_codeword

                codeword_start_index += 8
                codeword_final_index += 8

        print(group2_dict)

print(split_codewords(encode_data("HELLO WORLD", "Alphanumeric", "M"), 1, "M"))