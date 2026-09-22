def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    # Write code here

    n = len(values)
    ema = [0.0]*n

    ema[0] = values[0]

    for i in range(1,n):
        ema[i] += alpha * values[i] + (1- alpha)*ema[i-1]

    return ema