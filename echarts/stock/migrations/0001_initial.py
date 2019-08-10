# Generated by Django 2.2.4 on 2019-08-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('stock_ticker', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('stock_info', models.TextField()),
                ('stock_history', models.TextField()),
                ('stock_action', models.TextField()),
                ('stock_dividends', models.TextField()),
                ('stock_splits', models.TextField()),
                ('stock_financials', models.TextField()),
                ('stock_cashflow', models.TextField()),
                ('stock_options', models.TextField()),
            ],
        ),
    ]