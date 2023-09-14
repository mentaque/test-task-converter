import requests

api_key = '3vrSAI3Ovq489zwBZbjaPse4SQpGGxll'  # Замените на ваш ключ API от apilayer


def convert(to_coin, from_coin, amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_coin}&from={from_coin}&amount={amount}"

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    data = response.json()
    return data.get('result')
