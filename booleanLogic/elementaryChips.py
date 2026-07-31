from typing import Literal
from utilities.utils import Nand # the building block of this project

def Not(a: Literal[0,1]) -> Literal[0,1]:
    '''
    performs not operation on input

    Args:
        a - 1 bit value

    Returns:
        output is negation of a i.e., a'
    '''
    if a not in (0,1):
        raise ValueError("Value must be 0 or 1")

    val = Nand(a=a,b=a)
    return val

