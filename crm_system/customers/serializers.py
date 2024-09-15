from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'age', 'education', 'major', 'phone_number', 'wechat_id', 'initial_notes', 'last_edited', 'edit_count']  # 确保新字段包含在内