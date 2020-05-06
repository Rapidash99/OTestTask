import requests
import datetime
import redis
import json
from rest_framework import generics
from math import sqrt

from .models import Rate, Rates, Metric, Metrics
from .serializers import MetricsListSerializer


class MetricsListView(generics.ListAPIView):
    serializer_class = MetricsListSerializer

    def get_queryset(self):
        q_start_at = self.request.query_params.get('start_at')
        q_end_at = self.request.query_params.get('end_at')
        q_base = self.request.query_params.get('base')

        date_format = '%Y-%m-%d'

        # default values
        if q_start_at is None:
            q_start_at = '1999-01-04'
        q_start_at = datetime.datetime.strptime(q_start_at, date_format).date()

        if q_end_at is None:
            q_end_at = datetime.date.today()
        else:
            q_end_at = datetime.datetime.strptime(q_end_at, date_format).date()

        if q_base is None:
            q_base = 'EUR'

        # if bd already have requested metrics, just return them
        cached = Metrics.objects.filter(start_at=q_start_at, end_at=q_end_at, base=q_base)
        if len(cached) != 0:
            return cached

        r = redis.Redis()
        url = 'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}'
        cached = 'start_at:' + q_start_at.strftime(date_format) + 'end_at:' + q_end_at.strftime(date_format) + 'base:' + q_base

        # if the response from exchangeratesapi cached in Redis, take it
        if r.exists(cached):
            response = json.loads(r.get(cached).decode('utf8').replace("'", '"'))
        # or request from exchangeratesapi, and then cache in Redis
        else:
            response = requests.get(url.format(q_start_at, q_end_at, q_base)).json()
            r.set(cached, response.__str__())

        # create or get Rate and Rates objects
        for (r_date, r_rates) in response['rates'].items():
            rates = Rates.objects.get_or_create(base=response['base'], date=r_date)
            for (r_base, r_value) in r_rates.items():
                if not Rate.objects.filter(base=r_base, value=r_value, rates=rates[0]).exists():
                    Rate.objects.create(base=r_base, value=r_value, rates=rates[0])

        # get the set of Rates that are need to use
        rates_set = Rates.objects\
            .filter(date__gte=q_start_at)\
            .filter(date__lte=q_end_at)\
            .filter(base=q_base)

        # create dictionary of rates and their values in format (base -> [value])
        rates_dic = {}
        for rates in rates_set:
            for rate in rates.rates.all():
                if rate.base in rates_dic:
                    rates_dic[rate.base].append(rate.value)
                else:
                    rates_dic[rate.base] = [rate.value]

        # create requested metrics or get from db
        metrics = Metrics.objects.get_or_create(start_at=q_start_at, end_at=q_end_at, base=q_base)[0]

        # calculate metrics for this object
        for (base, values) in rates_dic.items():
            avg = 0
            for value in values:
                avg += value
            avg /= len(values)

            std_dev = 0
            for value in values:
                std_dev += (value - avg) ** 2
            std_dev = sqrt(std_dev / avg)

            Metric.objects.get_or_create(std_dev=std_dev, avg=avg, metrics=metrics, base=base)

        return Metrics.objects.filter(id=metrics.id)
