from django.contrib import admin
from django.db.models import Count
from . import models
# Register your models here.

class InventoryFilter(admin.SimpleListFilter): #custom filter or ModelAdmin List filters
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>10', 'OK')
        ]
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        if self.value() == '>10':
            return queryset.filter(inventory__gt=10)
        
@admin.register(models.Product) #registered decorator
class ProductAdmin(admin.ModelAdmin): #Class ModelAdmin
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self, product): #computed columns
        if product.inventory < 10:
            return 'LOW'
        return 'OK'
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        queryset.update()

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 20
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer', 'payment_status']
    list_editable = ['payment_status']
# admin.site.register(models.Collection)
# admin.site.register(models.Product)
# admin.site.register(models.Customer)