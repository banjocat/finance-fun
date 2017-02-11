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


