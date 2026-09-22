import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    # Write code here
    arr = np.asarray(scores,dtype = float,copy = True)

    t = arr.shape[-1]

    mask = np.triu(np.ones((t,t),dtype = bool),k=1)

    arr[...,mask] = mask_value

    return arr