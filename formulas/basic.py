import math


def interest(gain, years):
    '''
    Interest formula with N = 1

    >>> interest(.01, 1)
    1.01
    '''
    return math.pow(1 + gain, years)

def compound(gain, compound_rate, years, sigs=2):
    '''
    compound interest with N = 1

    >>> compound(.08, 4, 5)
    1.49
    >>> compound(1, 4, 1)
    2.44
    >>> 100 * compound(.05, 1, 2)
    110.25
    '''
    rate = float(gain) / compound_rate
    result = math.pow(1 + rate, years * compound_rate)
    return round(result, sigs)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
