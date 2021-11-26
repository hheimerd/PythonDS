import requests
import sys
from bs4 import BeautifulSoup
from time import sleep 


def main():
    ticker = sys.argv[1]
    field = sys.argv[2]
    base_url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    
    response = requests.get(base_url, headers={'User-Agent': 'Custom'})
    response.raise_for_status()

    bs = BeautifulSoup(response.text, 'lxml')
    row = bs.find('span', string=field).parent.parent.parent
    cells = list(row.children)
    print(tuple(i.string or i.find('span').string for i in cells))

if __name__ == '__main__':
    try:
        main()
        sleep(5)
    except Exception as e:
        print('operation failed')