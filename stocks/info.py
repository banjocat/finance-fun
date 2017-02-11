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

def get_sp500_names():
    '''
    Gets an array of all sp500 stocks

    >>> symbols = get_sp500_names()
    >>> len(symbols)
    505
    '''
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select('table.wikitable.sortable tr > td:nth-of-type(1) a[rel="nofollow"]')
    symbols = [ x.string for x in result ]
    return symbols

def get_stock_price_data(stock):
    '''
    Gets stock data
    
    >>> stock = get_stock_price_data('GRUB')
    >>> stock['Status']
    u'SUCCESS'
    '''
    endpoint = 'http://dev.markitondemand.com/Api/v2/Quote/json'
    url = '%s?symbol=%s' % (endpoint, stock)
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    import doctest
    doctest.testmod()


