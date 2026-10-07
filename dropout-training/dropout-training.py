import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here

    x_arr = np.array(x,dtype = float)

    if p == 0.0:
        dropout_pattern = np.ones_like(x_arr,dtype = float)

        return x_arr * dropout_pattern , dropout_pattern

    if rng is not None:
        rand_vals = rng.random(x_arr.shape)
    else:
        rand_vals = np.random.random(x_arr.shape)

    scale = 1.0 / (1.0 - p)

    dropout_pattern = np.where(rand_vals < (1.0 - p ),scale,0.0)

    output = x_arr *  dropout_pattern

    return output,dropout_pattern
        