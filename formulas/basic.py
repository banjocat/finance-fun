import math


def interest(value, gain, years):
    '''
    >>> interest(100, .01, 1)
    101.0
    >>> interest(100, .01, 2)
    102.01
    '''
    return value * math.pow(1 + gain, years)

def principle_interest(gain, years):
    '''
    Interest formula with N = 1

    >>> principle_interest(.01, 1)
    1.01
    '''
    return math.pow(1 + gain, years)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
