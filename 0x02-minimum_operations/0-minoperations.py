def minOperations(n):
    """
    This function computes the minimum number
    of operations for task Copy All and Paste

    Args:
        n (integer): input value
    Return:
        returns the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n //= i
                factor_list.append(i)
    return sum(factor_list)
