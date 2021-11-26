import urllib.parse
import urllib.request
import sys
from bs4 import BeautifulSoup


def get_company_row(ticker,field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Custom'})
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    
    bs = BeautifulSoup(the_page, 'lxml')
    row = bs.find('span', string=field).parent.parent.parent
    cells = list(row.children)
    print(tuple(i.string or i.find('span').string for i in cells))

def main():
    try:
        get_company_row(sys.argv[1], sys.argv[2])
    except Exception as e:
        print('operation failed')

if __name__ == '__main__':
    main()