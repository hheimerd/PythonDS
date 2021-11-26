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

    company = get_company(argv[1])

    if company:
        print(company, get_stock(company))
    else:
        print("Unknown company")


def get_stock(company: str):
    company = company.lower().capitalize()

    if company in COMPANIES:
        return STOCKS[COMPANIES[company]]
    return None


def get_company(ticker: str):
    ticker = ticker.upper()

    for key, val in COMPANIES.items():
        if val == ticker:
            return key
    return None


if __name__ == '__main__':
    main()
