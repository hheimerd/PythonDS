import requests
import sys
from bs4 import BeautifulSoup
import pytest


def get_company_row(ticker,field):
    base_url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    
    response = requests.get(base_url, headers={'User-Agent': 'Custom'})
    response.raise_for_status()

    bs = BeautifulSoup(response.text, 'lxml')
    row = bs.find('span', string=field).parent.parent.parent
    cells = list(row.children)
    return tuple(i.string or i.find('span').string for i in cells)

def main():
    try:
        result = get_company_row('tsla', 'Basic EPS')
        assert result[0] == 'Basic EPS'
        assert result.__class__ is tuple
        with pytest.raises(Exception):
            get_company_row('foo', 'bar')

    except AssertionError:
        print('test failed')

    except Exception as e:
        print('operation failed')
    
    else:
        print('test completed')


if __name__ == '__main__':
    main()