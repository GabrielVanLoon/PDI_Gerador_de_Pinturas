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
