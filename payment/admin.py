from django.contrib import admin

from payment.models import Item


# Register your models here.
@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'price',)
