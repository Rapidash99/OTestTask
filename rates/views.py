import requests
import datetime
import redis
from rest_framework import generics

from .models import Rate, Rates
from .serializers import RatesListSerializer, RateTestSerializer

'''
TODO: 
    start_at
    end_at
    base
    ~symbols~
    delete queryset from class???
'''


class RatesListView(generics.ListAPIView):
    serializer_class = RatesListSerializer
    queryset = Rates.objects.all()

    def get_queryset(self):
        queryset = Rates.objects.all()

        start_at = self.request.query_params.get('start_at')
        end_at = self.request.query_params.get('end_at')
        base = self.request.query_params.get('base')

        # default values
        if start_at is None:
            start_at = '1999-01-04'

        if end_at is None:
            end_at = datetime.date.today()

        if base is None:
            base = 'EUR'

        url = 'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}'
        response = requests.get(url.format(start_at, end_at, base)).json()

        r = redis.Redis()
        r.mset({'test1': '1', 'test2': '2'})
        print(r.get('test2'))

        counter = 0
        for (date, r) in response['rates'].items():
            print(counter)
            counter += 1

            rates = Rates.objects.get_or_create(base=response['base'], date=date)
            for (b, v) in r.items():
                Rate.objects.get_or_create(base=b, value=v, rates=rates[0])

        return queryset\
            .filter(date__gte=start_at)\
            .filter(date__lte=end_at)\
            .filter(base=base)


# test views


class RateCreateView(generics.CreateAPIView):
    serializer_class = RateTestSerializer
    queryset = Rate.objects.all()


class RatesCreateView(generics.CreateAPIView):
    serializer_class = RatesListSerializer
    queryset = Rates.objects.all()


class RateListView(generics.ListAPIView):
    serializer_class = RateTestSerializer
    queryset = Rate.objects.all()
