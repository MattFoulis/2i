
def multiples(A, X, A_mod = 0, X_mod = 0):
    """Creates and returns a list of multiples of A until X, with modifications to 
    one or both if required. 

    Args:
        A: The value to find multiples of
        X: The upper bounds for multiples
        A_mod: Modifications required for A
        X_mod: Modifications required for X

    Returns:
        A list of the multiples of A, up to and including X. 
    """

    if X == 0:
        return []

    results = [] # Stores each increment of A
    current = A # Tracks current value of A whilst iterating 

    # Apply modification. No change if none provided.
    if X_mod != 0:
        X *= X_mod
    current += A_mod

    # And new number to results then adjust A.
    while current <= X:
        results.append(current)
        current += A
        current += A_mod

    return results
