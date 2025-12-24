from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Product) #registered decorator
class ProductAdmin(admin.ModelAdmin): #Class ModelAdmin
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product): #computed columns
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_per_page = 5

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 20
    ordering = ['first_name', 'last_name']
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer', 'payment_status']
    list_editable = ['payment_status']
# admin.site.register(models.Collection)
# admin.site.register(models.Product)
# admin.site.register(models.Customer)