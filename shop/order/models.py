from django.db import models

from accounts.models import CustomUser, Addresses
from main.models import Product


# Create your models here.

class Order(models.Model):
    STATUS = [
        ('penging', 'В Обработке'),
        ('paid', 'Оплачен'),
        ('canceled', 'Отменён'),
        ('deliveres', 'Доставлен'),
        ('on the way', 'В Пути')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=STATUS, default='pending')
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)

    def order_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        self.total_price = total
        self.save()
        return total

    def __str__(self):
        return f"Заказ {self.id} - {self.user} ({self.get_status_display()})"


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_proce(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"