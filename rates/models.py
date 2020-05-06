from django.db import models


class Rate(models.Model):
    base = models.TextField(verbose_name='base', db_index=True, max_length=3)
    value = models.FloatField(verbose_name='value', db_index=True, max_length=15)
    rates = models.ForeignKey('Rates', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['base', 'rates'], name='unique_rate')]


class Rates(models.Model):
    base = models.TextField(verbose_name='base', db_index=True, max_length=3)
    date = models.DateField(verbose_name='date', db_index=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['base', 'date'], name='unique_rates')]


class Metric(models.Model):
    base = models.TextField(verbose_name='base', db_index=True, max_length=3)
    std_dev = models.FloatField(verbose_name='std_dev', db_index=True, max_length=20)
    avg = models.FloatField(verbose_name='avg', db_index=True, max_length=20)
    metrics = models.ForeignKey('Metrics', on_delete=models.CASCADE, related_name='metrics')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['base', 'metrics'], name='unique_metric')]


class Metrics(models.Model):
    base = models.TextField(verbose_name='base', db_index=True, max_length=3)
    start_at = models.DateField(verbose_name='date', db_index=True)
    end_at = models.DateField(verbose_name='date', db_index=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['base', 'start_at', 'end_at'], name='unique_metrics')]
