import imageio
import numpy as np
import matplotlib.pyplot as plt

from src.quantization import image_bitshift 

def visualize_bitshift_images(image):
    """
    Plot a 4x2 image grid aplying bitshifts in each plot position.
    """
    plt.figure(figsize=(40,40))
    for i in range(8):
        plt.subplot(420+i+1)
        plt.imshow(image_bitshift(image, bits=8-i, shift_return=True))
        plt.title(f"({8-i} BIT)")
