import math


def interest(rate, years):
    '''
    Interest formula with N = 1

    >>> val = interest(.01, 1)
    >>> round(val, 2)
    1.01
    '''
    return math.pow(1 + rate, years)

def compound(rate, compound_amount, years):
    '''
    compound interest with N = 1

    >>> val = compound(.08, 4, 5)
    >>> round(val, 2)
    1.49
    >>> val = compound(1, 4, 1)
    >>> round(val, 2)
    2.44
    >>> val = 100 * compound(.05, 1, 2)
    >>> round(val, 2)
    110.25
    '''
    rate = float(rate) / compound_amount
    result = math.pow(1 + rate, years * compound_amount)
    return result

def continous_compound(rate, years):
    '''
    theortical continous compound rate

    >>> val = continous_compound(.05, 1)
    >>> round(val, 4)
    1.0513
    >>> val = continous_compound(.05, 2)
    >>> round(val, 4)
    1.1052
    >>> val = continous_compound(.08, 5)
    >>> round(val, 4)
    1.4918
    '''
    rT = rate * years
    return math.pow(math.e, rT)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
