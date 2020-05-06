from rest_framework import serializers
from .models import Rate, Rates, Metric, Metrics


class RateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('base', 'value')


class RatesListSerializer(serializers.ModelSerializer):
    rates = RateListSerializer(many=True)

    class Meta:
        model = Rates
        fields = ('base', 'date', 'rates')


class MetricListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ('base', 'std_dev', 'avg')


class MetricsListSerializer(serializers.ModelSerializer):
    metrics = MetricListSerializer(many=True)

    class Meta:
        model = Metrics
        fields = ('base', 'start_at', 'end_at', 'metrics')
