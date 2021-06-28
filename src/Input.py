#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imageio
import numpy as np
import matplotlib.pyplot as plt

# funcao que carrega a imagem
def load_img(imgPath):
    """
    Receive a image path and return a numpy array with with type np.uint8.
    """

    # leitura inicial da imagem
    imgRaw = imageio.imread(imgPath)
    
    # type(imgRaw) -->  <class 'imageio.core.util.Array'>
    
    
    img2 = np.zeros(imgRaw.shape, dtype=np.uint8)
    
    # tipo do img2 -->  <class 'numpy.ndarray'>
    # tipo do img2[0,0,0] --> <class 'numpy.uint8'>

    for x in range(imgRaw.shape[0]):
        for y in range(imgRaw.shape[1]):
            img2[x,y] = imgRaw[x,y]
    
    return img2




### Leitura do path da imagem

# instrucao para o usuario do que ele deve digitar
print ("Forneça o Path da imagem")

# exemplos que funcionam para facilitar a execucao
print ("Exemplos válidos: ")
print ("../images/raw/anime_girl.png")
print ("../images/raw/grayscale_selfie.png")

# leitura de string
imgPath = input().rstrip()

# chamada de funcao que carrega imagem
imgRaw = load_img(imgPath)



### exibicao da imagem para verificar resultado
plt.imshow(imgRaw)

# armazenando as dimensoes da imagem
shapeN = imgRaw.shape[0]
shapeM = imgRaw.shape[1]

# exibicao das dimensoes da imagem
print (shapeN, shapeM)

