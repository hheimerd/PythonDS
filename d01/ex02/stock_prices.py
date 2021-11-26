import sys

COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
}
STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}


def main():

    argv = sys.argv
    if len(argv) != 2:
        return

    stock = get_stock(argv[1])

    if stock:
        print(stock)
    else:
        print("Unknown company")


def get_stock(company):
    company = company.lower().capitalize()

    if company in COMPANIES:
        return STOCKS[COMPANIES[company]]
    return None


if __name__ == '__main__':
    main()
