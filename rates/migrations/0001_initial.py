# Generated by Django 3.0.6 on 2020-05-04 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.TextField(db_index=True, max_length=3, verbose_name='base')),
                ('value', models.FloatField(db_index=True, max_length=6, verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.TextField(db_index=True, max_length=3, verbose_name='base')),
                ('date', models.DateField(db_index=True, verbose_name='date')),
                ('rates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rates.Rate')),
            ],
        ),
    ]
