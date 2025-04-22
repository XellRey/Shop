from django.contrib import admin
from .models import Order, OrderItems
#Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created", "total_price", "status")
    list_filter = ("status", "created")
    inlines = [OrderItemInline]

admin.site.register(OrderItems)