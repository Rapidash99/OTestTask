# Generated by Django 3.0.6 on 2020-05-04 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_auto_20200505_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='rates.Rates'),
        ),
    ]