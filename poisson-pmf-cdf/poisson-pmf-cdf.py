import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here

    pmf = (math.exp(-lam)) * (lam ** k) / math.factorial(k)

    cdf = sum((math.exp(-lam)) * (lam ** k) / math.factorial(k)
              for k in range(0,k+1)
             )

    return {
        "pmf" : float(pmf),
        "cdf" : float(cdf),
    }