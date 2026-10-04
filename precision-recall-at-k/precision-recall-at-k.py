def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here

    relevant_set = set(relevant)
    top_k = recommended[:k]

    hits = sum(1 for item in top_k if item in relevant_set)

    precision = hits / k
    recall = hits / len(relevant_set)

    return [precision, recall]
    