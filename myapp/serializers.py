from rest_framework import serializers
from .models import item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ['id', 'item_name', 'item_price', 'item_desc', 'item_image', 'is_available', 'created_at']