import requests
from lxml import html
from bs4 import BeautifulSoup


def get_nasdaq_names():
    '''
    Gets an array of all nasdaq stocks

    >>> symbols = get_nasdaq_names()
    >>> len(symbols)
    105
    '''
    url = 'http://www.cnbc.com/nasdaq-100'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select('td[data-field="symbol"] a')
    symbols = [ x.text for x in result ]
    return symbols


if __name__ == '__main__':
    import doctest
    doctest.testmod()


