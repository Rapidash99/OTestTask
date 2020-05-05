from rest_framework import serializers
from .models import Rate, Rates


class RateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('base', 'value')


class RatesListSerializer(serializers.ModelSerializer):
    rates = RateTestSerializer(many=True)

    class Meta:
        model = Rates
        fields = ('base', 'date', 'rates')
        # read_only_fields =
