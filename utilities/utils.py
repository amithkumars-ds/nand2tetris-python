from typing import Literal

# preset
Bit = Literal['0','1']
Word16 = str
Word8 = str

sel2 = Literal["00", "01", "10", "11"]
sel3 = Literal["000", "001", "010", "011",
               "100", "101", "110", "111"]

def Nand(a:Bit, b:Bit) -> Bit:  # the building block of this project
    '''
    implementing a basic Nand gate

    Args:
        a - 1 bit value
        b - 1 bit value
    
    Returns:
        output - 1 bit value of (ab)'
    '''
    
    _check_bits(a,b)

    out = "0" if a == "1" and b == "1" else "1"
    
    return out

def _check_bits(*bits: int) -> None:
    if any(bit not in ('0', '1') for bit in bits):
        raise ValueError("Values must be 0 or 1")

def _check_length(bits:str, size: int) -> None:
    if len(bits) != size:
        raise ValueError(f"Given input is not of length: {size}")

def bits_to_binary(binary: str) -> list[str]:
    _check_bits(*binary)
    return list(binary)

def binary_to_bits(bits: list[Bit]) -> Word16:
    _check_bits(*bits)
    return ''.join(bits)