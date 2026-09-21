import numpy as np



def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    arr = np.asarray(x,dtype = float)
    x_max = np.max(x,axis = -1 , keepdims = True)

    exp_shifted = np.exp(arr - x_max)

    p = exp_shifted / np.sum(exp_shifted,axis = -1,keepdims = True)

    return p
    
    