from django.contrib import admin
from apps.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',  'created_at')
    list_display_links = ('id', 'name', 'price')


admin.site.register(Product, ProductAdmin)
