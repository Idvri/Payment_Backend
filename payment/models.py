from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Цена'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        verbose_name='Заказ',
        related_name='items',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
