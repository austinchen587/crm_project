from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        # 创建客户时，不需要特别处理，默认会添加创建时间
        serializer.save()

    def perform_update(self, serializer):
        # 更新客户时自动更新最后编辑时间和编辑次数
        instance = serializer.save()
        instance.last_edited = timezone.now()
        instance.edit_count += 1
        instance.save()
