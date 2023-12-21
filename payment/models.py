from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
