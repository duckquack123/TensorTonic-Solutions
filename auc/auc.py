import numpy as np

def auc(fpr: list, tpr: list) -> float:
    """
    Returns the area as a float.
    """
    # Write code here

    x = np.asarray(fpr, dtype = float)
    y = np.asarray(tpr, dtype = float)

    order = np.argsort(x)
    x = x[order]
    y = y[order]

    dx = np.diff(x)

    avg_y = (y[:-1] + y[1:]) / 2.0

    area = np.sum(dx * avg_y)

    return float(area)

    