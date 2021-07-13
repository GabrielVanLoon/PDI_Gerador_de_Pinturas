import imageio
import numpy as np
from sklearn.cluster import KMeans

def image_bitshift(image, bits=8, shift_return=False):
    """
    Receive a image and return a copy with the values in range [0,2^bits]. If
    @shift_return is True return the bits to the most significant bits.
    """
    output = np.copy(image)
    output = output >> (8 - bits)
    output = output << (8 - bits) if shift_return else output
    return output


def palette_kmeans(image, N):
    """
    Use Kmeans learning method to get a collor pallete of N
    colors. Also return the recolorized image, label map and the model
    
    Returns:
        palette, image_recolorized, labels_map, kmeans
    """

    # Pré-proccess: precisamos mudar a imagem de (N,N,3) p/ (N²,3)
    image_inline =  image.reshape(-1,3)
    
    # Training the model
    kmeans = KMeans(n_clusters=N, max_iter=300)
    kmeans.fit(image_inline)
    
    # Return Collor pallete (np.array)
    palette = kmeans.cluster_centers_
    
    # Reconstruct the image with the N colors
    image_labels = kmeans.predict(image_inline)
    image_labels = image_labels.reshape((image.shape[0], image.shape[1]))
    image_output = np.zeros(image.shape)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_output[i,j,:] = palette[image_labels[i,j]]
    
    return palette, image_output, image_labels, kmeans



# Search for anothers interesting methods :)