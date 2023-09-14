from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from converter_app.serializers import CurrencyConverterSerializer
from converter_app.api import convert


class CurrencyConverter(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('from', openapi.IN_QUERY, description="Код исходной валюты", type=openapi.TYPE_STRING),
            openapi.Parameter('to', openapi.IN_QUERY, description="Код целевой валюты", type=openapi.TYPE_STRING),
            openapi.Parameter('value', openapi.IN_QUERY, description="Сумма для конвертации", type=openapi.TYPE_NUMBER),
        ]
    )
    def get(self, request):
        data = {
            'from_currency': request.query_params.get('from', ''),
            'to_currency': request.query_params.get('to', ''),
            'value': request.query_params.get('value', ''),
        }

        serializer = CurrencyConverterSerializer(data=data)

        if serializer.is_valid():
            from_currency = serializer.validated_data['from_currency']
            to_currency = serializer.validated_data['to_currency']
            value = serializer.validated_data['value']

            converted = convert(to_currency, from_currency, value)

            if converted:
                return Response({'result': converted})
            else:
                return Response({'error': 'Не удалось получить данные с apilayer,'
                                          ' проверьте правильность введенных данных'})
        else:
            return Response({'error': 'Неверные входные данные'})