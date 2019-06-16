from rest_framework import serializers
from shop.models import Category, Product


class ShopSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = "__all__"