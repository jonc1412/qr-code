from .constants import ERROR_CORRECTION
from .poly_functions import poly_mult
from .gf_functions import exp_table

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

            for codeword_num in range(num_codewords_group2):
                current_codeword = data[codeword_start_index:codeword_final_index]
                split_dict[2][block_num+1].append(current_codeword)

                codeword_start_index += 8
                codeword_final_index += 8

    return split_dict

def get_num_list(binary_list : list) -> list:
    num_list = []

    for codeword in binary_list:
        num_list.append(int(codeword, 2))
    
    num_list.reverse()

    return num_list

def generate_message_polynomial(data_dict : dict):
    message_polynomial = dict()

    for group_num, block_codewords in data_dict.items():
        message_polynomial[group_num] = dict()

        for block_num, codeword_list in block_codewords.items():
            message_polynomial[group_num][block_num] = get_num_list(codeword_list)

    return message_polynomial

def generate_generator_polynomial(qr_version : int, err_corr : str) -> list[int]:
    codewords_count = ERROR_CORRECTION[f'{qr_version}-{err_corr}']['ec_codewords_per_block']
    gen_poly = [1]
    print(codewords_count)

    for i in range(codewords_count):
        gen_poly = poly_mult(gen_poly, [1, exp_table[i]])
    
    return gen_poly

print(generate_generator_polynomial(1, "M"))