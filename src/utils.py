import imageio
import numpy as np
import math


def load_image(image_path):
    """
    Receive a image path and return a numpy array with with type np.uint8.
    """
    return imageio.imread(image_path).astype(np.uint8)

def save_image(image, image_path):
    """
    Receive a image and a image_path and save into the disk. Raise a error if
    the image path is arealdy used by another file.
    """
    return None 

def image_downsampling(image, max_size=1024):
    """
    Receive a image and return a copy with preserved proportions and max width
    or height equal or less @max_size. Return the copy to the user.
    Implemented methods: 'avg', 'median', 'min', 'max'
    """
    # armazenando as dimensoes da imagem
    shapeN = image.shape[0]
    shapeM = image.shape[1]
    comp = image.shape[2]
    
    if shapeN <= max_size and shapeM <= max_size:
        # se as dimensoes da imagem já são menores do que max_size
        # retorna a imagem, sem fazer alteracoes
        return image
    
    # se o lado maior eh N (formato retrato)
    if shapeN > shapeM:
        # descobrindo a dimensao da nova imagem
        newN = max_size
        newM = math.floor(newN / shapeN * shapeM)
    # se o lado maior eh M (formato paisagem)
    else:
        # descobrindo a dimensao da nova imagem
        newM = max_size
        newN = math.floor(newM / shapeM * shapeN)
        
    # Criacao da imagem amostrada (sampling) de tamanho newN x newM 
    imageSamp = np.zeros((newN,newM,comp)).astype(np.uint8)

    # preenchimento da nova imagem
    stepX = shapeN/float(newN)
    stepY = shapeM/float(newM)
    for x in range(newN):
        for y in range(newM):
            imageSamp[x,y] = image[math.floor(x*stepX),math.floor(y*stepY)]
    
    return imageSamp

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

def image_to_grayscale(image):
    """
    Receive a image turn it to grayscale using the luminance method.
    """
    output = np.floor(0.299*image[:,:,0] + 0.587*image[:,:,1] + 0.114*image[:,:,2]).astype(np.uint8)
    return output