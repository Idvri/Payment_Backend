from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class ValueFor(models.Model):
    value = models.IntegerField(unique=True, verbose_name='значение (процент)')


class Tax(ValueFor):

    def __str__(self):
        return f'{self.value}%'

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'


class Discount(ValueFor):

    def __str__(self):
        return f'{self.value}%'

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Order(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, verbose_name='Налог', null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, verbose_name='Скидка', null=True, blank=True)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
