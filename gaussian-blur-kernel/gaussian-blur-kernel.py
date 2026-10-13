import math
import numpy as np

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    center = size // 2

    y , x = np.ogrid[-center:size-center , -center:size-center]

    kernel = np.exp(-(x**2+y**2) / (2 * sigma **2))

    kernel = kernel / np.sum(kernel)

    return kernel.tolist()

    
    
    
    