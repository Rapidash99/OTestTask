from django.db import models
from datetime import datetime

# 16:00 CET
# 17:00 UTC+3


class Rate(models.Model):
    base = models.TextField(verbose_name='base', db_index=True, max_length=3)
    value = models.FloatField(verbose_name='value', db_index=True, max_length=6)
    rates = models.ForeignKey('Rates', on_delete=models.CASCADE, related_name='rates')

    # def


class Rates(models.Model):
    base = models.TextField(verbose_name='base', db_index=True, max_length=3)
    date = models.DateField(verbose_name='date', db_index=True)  # default?
