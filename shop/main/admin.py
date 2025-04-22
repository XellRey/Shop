from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Category)
class CatrgoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category')
    search_fields = ('name', 'category')