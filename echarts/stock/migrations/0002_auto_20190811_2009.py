# Generated by Django 2.2.4 on 2019-08-11 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticker',
            old_name='stock_action',
            new_name='stock_actions',
        ),
        migrations.RenameField(
            model_name='ticker',
            old_name='stock_dividends',
            new_name='stock_balance_sheet',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='stock_splits',
        ),
    ]