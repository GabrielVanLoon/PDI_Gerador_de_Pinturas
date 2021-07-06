import numpy as np

def threshold_segmentation(gray_image, threshold=128, value=255):
    """
    Receive a grayscale image and perform a basic threshold segmentation
    that returns: 
        - 0      where i <  threshold
        - value  where i >= threshold
    """
    output = np.copy(gray_image)
    output = np.where(output >= threshold, value, 0)
    return output

def otsu_segmentation(gray_image, value=255):
    """
    Receive a grayscale image and perform the otsu segmentation method that
    returns:
        - 0      where i <  threshold
        - value  where i >= threshold
    """
    min_var = []
    hist, _ = np.histogram(gray_image, bins=256, range=(0,256))

    for L in np.arange(1,np.max(gray_image)+1):
        img_ti = threshold_segmentation(gray_image, threshold=L, value=1)
        w_a = np.sum(hist[:L])/float(gray_image.size)
        w_b = np.sum(hist[L:])/float(gray_image.size)
        sig_a = np.var(gray_image[np.where(img_ti == 0)])
        sig_b = np.var(gray_image[np.where(img_ti == 1)])

        min_var = min_var + [w_a*sig_a + w_b*sig_b]
        
    output = threshold_segmentation(gray_image, threshold=np.argmin(min_var), value=value)
    return output, np.argmin(min_var)


def labels_to_edges(labels):
    """
    Receive a color label map and return a edge map where:
    - [i,j] == 1 if is edge
    - [i,j] == 0 if is not edge
    """

    # Pre-proccess: add symetric pad to avoid corners bugs
    edge_map = np.zeros(labels.shape, dtype=np.int32)
    labels   = np.pad(labels, 1, mode="symmetric")
    
    # Apply Laplacian filter to detect if any 8-neighboor is diff
    # not edge -> 0 (black)
    # edge     -> 1 (white)
    for i in range(1,labels.shape[0]-1):
        for j in range(1,labels.shape[1]-1):
            same_color = np.sum(labels[i-1:i+2,j-1:j+2] == labels[i,j]) != 9
            # print(i,j,same_color)
            # print(labels[i-1:i+2,j-1:j+2])
            edge_map[i-1, j-1] = same_color * 1
    
    return edge_map