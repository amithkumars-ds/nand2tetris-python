from typing import Literal

def Nand(a:Literal[0,1], b:Literal[0,1]) -> Literal[0,1]:  # the building block of this project
    '''
    implementing a basic Nand gate

    Args:
        a - 1 bit value
        b - 1 bit value
    
    Returns:
        output - 1 bit value of (ab)'
    '''
    
    _check_bits(a,b)

    operation = not(a and b)
    val = 1 if operation else 0
    
    return val

def _check_bits(*bits: int) -> None:
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("Values must be 0 or 1")

def _check_length(bits:list, size: int) -> None:
    if len(bits) != size:
        raise ValueError(f"Given input is not of length: {size}")

def bits_to_binary(binary: int) -> list[int]:
    bits = [int(bit) for bit in binary]
    return bits

def binary_to_bits(bits: list[int]) -> int:
    word = ''
    for bit in bits:
        word = word+str(bit)
    return int(word)