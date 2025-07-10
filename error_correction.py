from constants import ERROR_CORRECTION
from encoder import encode_data, get_version

def split_codewords(data : str, qr_version : int, err_corr : str):
    num_blocks_group1 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["num_blocks_group1"]
    num_codewords_group1 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["data_codewords_group1"]
    num_blocks_group2 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["num_blocks_group2"]
    num_codewords_group2 = ERROR_CORRECTION[f'{qr_version}-{err_corr}']["data_codewords_group2"]

    # print(f'Number of blocks in group 1: {num_blocks_group1} with {num_codewords_group1} codewords')
    # print(f'Number of blocks in group 2: {num_blocks_group2} with {num_codewords_group2} codewords')
    # print(f'The total number of codeword blocks: {num_blocks_group1 * num_codewords_group1 + num_blocks_group2 * num_codewords_group2}\n\n')

    split_dict = dict()
    split_dict[1] = dict()

    codeword_start_index = 0
    codeword_final_index = 8

    for block_num in range(num_blocks_group1):
        split_dict[1][block_num+1] = []

        for codeword_num in range(num_codewords_group1):
            current_codeword = data[codeword_start_index:codeword_final_index]
            split_dict[1][block_num+1].append(current_codeword)

            codeword_start_index += 8
            codeword_final_index += 8

    if num_blocks_group2 > 0:
        split_dict[2] = dict()

        for block_num in range(num_blocks_group2):
            split_dict[2][block_num+1] = []

            for j in range(num_codewords_group2):
                current_codeword = data[codeword_start_index:codeword_final_index]
                split_dict[2][block_num+1].append(current_codeword)

                codeword_start_index += 8
                codeword_final_index += 8

    return split_dict

# def generate_message_polynomial(codeword_dict):
#     message_polynomial = []

#     for group, codeword in codeword_dict:
#         for i in range(len(codeword)):
