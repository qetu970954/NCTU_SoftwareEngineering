from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'credit_card_number', 'expire_date', 'security_code',
                    'created', 'paid']
    list_filter = ['paid', 'created']
    list_editable = ['paid']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
