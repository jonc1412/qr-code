"""
QR Code Generator Package

A Python implementation of QR code generation with Reed-Solomon error correction.
"""

from .encoder import encode_data, encode_alphanumeric, get_version
from .constants import (
    MODE_INDICATOR, 
    ALPHANUMERIC_TABLE, 
    ERROR_CORRECTION, 
    CHAR_COUNT_INDICATOR_BITS,
    QR_CAPACITY
)
from .error_correction import split_codewords, get_num_list, generate_message_polynomial
from .gf_functions import add_sub, mult, div

__version__ = "0.1.0"
__author__ = "Jonathan Choi"

__all__ = [
    'encode_data',
    'encode_alphanumeric', 
    'get_version',
    'add_sub',
    'mult',
    'div',
    'MODE_INDICATOR',
    'ALPHANUMERIC_TABLE',
    'ERROR_CORRECTION',
    'CHAR_COUNT_INDICATOR_BITS',
    'QR_CAPACITY',
    'split_codewords',
    'get_num_list',
    'generate_message_polynomial'
]