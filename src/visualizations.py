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

def plot_pallete(palette, shape):
    """
    Receive a palette of colors (RGB) and a shape and plot it.
    """

    plt.figure(figsize=(12,1))
    for i in range(palette.shape[0]):
        plt.subplot(shape[0],shape[1],i+1)
        plt.axis("off")
        plt.imshow(np.ones((3,3,3), dtype=np.int)*palette[i].astype(np.int))

def plot_imagegrid(images, shape, figsize=(40,40)):
    """
    Receive a array of imagens, a shape and a figsize and plot it.
    """

    plt.figure(figsize=figsize)
    for i in range(len(images)):
        plt.subplot(shape[0],shape[1],i+1)
        plt.imshow(images[i].astype(np.int), cmap="gray")
