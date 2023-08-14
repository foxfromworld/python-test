def countOdds(low, high):
    """
    Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

    :type low: int
    :type high: int
    :rtype: int
    """
    if ( high%2 == 0 ) and ( low%2 == 0):
        return (high-low)/2
    return (high-low)//2 + 1
