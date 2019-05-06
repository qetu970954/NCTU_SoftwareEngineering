from datetime import datetime

from django.db import models
from shop.models import Product


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    credit_card_number = models.CharField(max_length=16, default="1234123412341234")
    expire_date = models.CharField(default="12/24", max_length=5)
    security_code = models.CharField(max_length=3, default="633")
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
