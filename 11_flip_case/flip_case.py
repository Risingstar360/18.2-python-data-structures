from os import lseek
from sysconfig import is_python_build


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    flipped = ""
    
    for ltr in phrase:
        if ltr == to_swap and ltr.upper() == to_swap:
            ltr.swapcase()
        flipped += ltr
    return flipped
        





