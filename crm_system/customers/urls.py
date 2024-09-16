from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import customer_note_history

router = routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('customers/<int:customer_id>/note_history/', customer_note_history),
]