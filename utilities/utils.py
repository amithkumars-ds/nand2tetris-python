from typing import Literal

def Nand(a:Literal[0,1], b:Literal[0,1]) -> Literal[0,1]:
    '''
    implementing a basic Nand gate

    Args:
        a - 1 bit value
        b - 1 bt value
    
    Returns:
        output - 1 bit value of (ab)'
    '''
    if a and b not in (0,1):
        raise ValueError('Values must be 0 or 1')
    
    operation = not(a and b)
    val = 1 if operation else 0
    
    return val
