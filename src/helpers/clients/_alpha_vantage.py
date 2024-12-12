def main():
    import requests
    from decouple import config

    ALPHAVANTAGE_API_KEY = config("ALPHAVANTAGE_API_KEY", default=None, cast=str) is not None

    params = {
        "api_key": ALPHAVANTAGE_API_KEY,
        "ticker": "AAPL",
        "function": "TIME_SERIES_INTRADAY",
        "minute": 1
    }

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function={function}&symbol={ticker}&interval={minute}min&apikey={api_key}'.format(**params)
    r = requests.get(url)
    data = r.json()
    dataset_key = [x for x in list(data.keys()) if not x.lower() == "meta data"][0]
    results = data[dataset_key]
    results.keys()
    return results

if __name__ == '__main__':
    print(main())