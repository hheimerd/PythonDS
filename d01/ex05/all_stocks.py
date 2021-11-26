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

    strings = list(map(lambda x: x.strip(' \n\t'), argv[1].split(",")))

    if '' in strings: return

    for request in strings:
        company = get_company(request)
        price = get_price(request)

        if company:
            print("{} is a ticker symbol for {}".format(request.upper(), company))
        elif price:
            print("{} stock price is {}".format(request.lower().capitalize(), price))
        else:
            print(request + " is an unknown company or an unknown ticker symbol")

   


def get_price(company: str):
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
