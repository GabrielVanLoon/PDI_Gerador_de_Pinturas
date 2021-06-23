import imageio
import numpy as np

def image_bitshift(image, bits=8, shift_return=False):
    """
    Receive a image and return a copy with the values in range [0,2^bits]. If
    @shift_return is True return the bits to the most significant bits.
    """
    output = np.copy(image)
    output = output >> (8 - bits)
    output = output << (8 - bits) if shift_return else output
    return output

# Search for anothers interesting methods :)