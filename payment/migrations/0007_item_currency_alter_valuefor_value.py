# Generated by Django 5.0 on 2023-12-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_order_discount_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('rub', 'RUB'), ('usd', 'USD'), ('eur', 'EUR')], default='usd', max_length=3, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='valuefor',
            name='value',
            field=models.IntegerField(unique=True, verbose_name='значение (процент)'),
        ),
    ]
