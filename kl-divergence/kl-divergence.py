import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here

    p = np.array(p,dtype = float)
    q = np.array(q,dtype = float)

    D_kl = np.sum(p*np.log((p+eps)/(q+eps)))

    return D_kl.item()