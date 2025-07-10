from constants import ERROR_CORRECTION
from encoder import encode_data, get_version

def split_codewords(data, qr_version , err_corr):
    num_blocks_group1 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["num_blocks_group1"]
    num_codewords_group1 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["data_codewords_group1"]
    num_blocks_group2 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["num_blocks_group2"]
    num_codewords_group2 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["data_codewords_group2"]

    print(f'Number of blocks in group 1: {num_blocks_group1} with {num_codewords_group1} codewords')
    print(f'Number of blocks in group 2: {num_blocks_group2} with {num_codewords_group2} codewords')
    print(f'The total number of codeword blocks: {num_blocks_group1 * num_codewords_group1 + num_blocks_group2 * num_codewords_group2}\n\n')

    split_dict = dict()
    split_dict[1] = []

    codeword_start_index = 0
    codeword_final_index = 8

    for i in range(num_blocks_group1):
        for j in range(num_codewords_group1):
            current_codeword = data[codeword_start_index:codeword_final_index]
            split_dict[1].append(current_codeword)

            codeword_start_index += 8
            codeword_final_index += 8

    if num_blocks_group2 > 0:
        split_dict[2] = []

        for i in range(num_blocks_group2):
            for j in range(num_codewords_group2):
                current_codeword = data[codeword_start_index:codeword_final_index]
                split_dict[2].append(current_codeword)

                codeword_start_index += 8
                codeword_final_index += 8

    return split_dict