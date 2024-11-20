def main():
    import requests
    from decouple import config
    POLOGYON_API_KEY = config("POLOGYON_API_KEY", default=None, cast=str)
    ticker = "AAPL"
    multiplier = "4"
    timespan = "minute"
    from_date = "2023-01-09"
    to_date = "2023-01-09"
    path = f"/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    url = f'https://api.polygon.io/{path}?apiKey={POLOGYON_API_KEY}'
    response = requests.get(url)
    result = response.json()
    return result['results'][0]


def transform_polygon_result(results):
    import pytz
    from datetime import datetime
    unix_timestamp = results.get('t') / 1000.0
    utc_timestamp = datetime.fromtimestamp(unix_timestamp, tz=pytz.timezone('UTC'))
    return {
        'open_price': results['o'],
        'close_price': results['c'],
        'high_price': results['h'],
        'low_price': results['l'],
        'number_of_trades': results['n'],
        'volume': results['v'],
        'volume_weighted_average': results['vw'],
        'time': utc_timestamp,
    }


if __name__ == '__main__':
    result = main()
    print(transform_polygon_result(result))
