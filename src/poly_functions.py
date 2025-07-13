from .gf_functions import add_sub, mult

def poly_mult(p1 : list[int], p2 : list[int]) -> list[int]:
    result = [0] * (len(p1) + len(p2) - 1)

    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] = add_sub(result[i + j], mult(p1[i], p2[j]))
        
    return result