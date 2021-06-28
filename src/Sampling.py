#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import imageio
import numpy as np
import math

# caso alguma das dimensoes da imagem seja maior do que maxSize
# reduz as dimensoes da imagem
def sampling (img, maxSize = 1000):
    
    # armazenando as dimensoes da imagem
    shapeN = img.shape[0]
    shapeM = img.shape[1]
    comp = img.shape[2]
    
    if shapeN <= maxSize and shapeM <= maxSize:
        # se as dimensoes da imagem já são menores do que maxSize
        # retorna a imagem, sem fazer alteracoes
        return img
    
    # se o lado maior eh N (formato retrato)
    if shapeN > shapeM:
        # descobrindo a dimensao da nova imagem
        newN = maxSize
        newM = math.floor(newN / shapeN * shapeM)
    # se o lado maior eh M (formato paisagem)
    else:
        # descobrindo a dimensao da nova imagem
        newM = maxSize
        newN = math.floor(newM / shapeM * shapeN)
        
    # Criacao da imagem amostrada (sampling) de tamanho newN x newM 
    imgSamp = np.zeros((newN,newM,comp)).astype(np.uint8)


    # preenchimento da nova imagem
    step = shapeN/float(newN)
    for x in range(newN):
        for y in range(newM):
            imgSamp[x,y] = img[math.floor(x*step),math.floor(y*step)]
    
    return imgSamp

