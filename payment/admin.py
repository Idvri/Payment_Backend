from django.contrib import admin

from payment.models import Item, Order


# Register your models here.
@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'price',)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('name',)
