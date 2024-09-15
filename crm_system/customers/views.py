from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def update(self, request, *args, **kwargs):
        customer = self.get_object()
        data = request.data

        #手动更新编辑时间和编辑次数
        customer.last_edited = timezone.now()
        customer.edit_count += 1
        
        serializer = CustomerSerializer(customer,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

