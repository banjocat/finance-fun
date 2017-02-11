import math


def interest(gain, years):
    '''
    Interest formula with N = 1

    >>> round(interest(.01, 1), 2)
    1.01
    '''
    return math.pow(1 + gain, years)

def compound(gain, compound_rate, years):
    '''
    compound interest with N = 1

    >>> round(compound(.08, 4, 5), 2)
    1.49
    >>> round(compound(1, 4, 1), 2)
    2.44
    >>> round(100 * compound(.05, 1, 2), 2)
    110.25
    '''
    rate = float(gain) / compound_rate
    result = math.pow(1 + rate, years * compound_rate)
    return result



if __name__ == '__main__':
    import doctest
    doctest.testmod()
