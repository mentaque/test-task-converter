# Currency Converter API

Это простой RESTful API, созданный с использованием Django и Django REST framework, который позволяет выполнять конвертацию валют(иногда долгое ожидание ответа от сервера!)

## Описание

API предоставляет возможность конвертировать сумму из одной валюты в другую, используя данные от сервиса apilayer. Для теста и дебага использовался swagger `http://127.0.0.1:8000/swagger/`

## Инструкции по установке и запуску

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/mentaque/currency-converter-api.git

2. Установите зависимости:
   
   ```bash
   pip install -r requirements.txt

3. Перейдите в папку main:

   ```bash
   cd main

4. Запустите сервер:

   ```bash
   python manage.py runserver

API будет доступно по адресу `http://localhost:8000/api/rates/`

## Использование 

Для выполнения конвертации валюты, отправьте GET-запрос на /api/rates/ с параметрами from, to, и value. Например:
`GET /api/rates/?from=USD&to=RUB&value=1`
