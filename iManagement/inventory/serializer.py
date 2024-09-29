from rest_framework import serializers
from .models import Items
from typing import Any

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields:Any = "__all__"
    

