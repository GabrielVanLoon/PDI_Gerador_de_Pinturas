import imageio
import numpy as np


def load_image(image_path):
    """
    Receive a image path and return a numpy array with with type np.uint8.
    """
    return None

def save_image(image, image_path):
    """
    Receive a image and a image_path and save into the disk. Raise a error if
    the image path is arealdy used by another file.
    """
    return None 

def image_downsamplinng(image, max_size=1024, method="avg"):
    """
    Receive a image and return a copy with preserved proportions and max width
    or height equal or less @max_size. Return the copy to the user.
    Implemented methods: 'avg', 'median', 'min', 'max'
    """
    return None 

def image_minmax_norm(image, max=255):
    """
    Perform a minmax normalization and return a normalized copy of the image to the
    new range [0,max]
    """
    imin, imax = (np.min(image), np.max(image))
    output = np.copy(image)
    output = ((output - imin)/(imax - imin)) * max
    return output.astype(np.uint8)

def image_pixel_clip(image, min=0, max=255):
    """
    Clip values to between [min,max] range and return.
    """
    output = np.clip(np.copy(image), min, max)  
    return output.astype(np.uint8)