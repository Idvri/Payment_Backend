from django.contrib import admin

from payment.models import Item, Order, Discount, Tax


# Register your models here.
@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'price',)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tax)
class AdminOrder(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Discount)
class AdminOrder(admin.ModelAdmin):
    list_display = ('value',)
