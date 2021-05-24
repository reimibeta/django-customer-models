from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from customer_models import views

router = routers.DefaultRouter()
""" Pre Build Orders api """
router.register('customer', views.CustomerViewSet)
router.register('customer-phone', views.CustomerPhoneViewSet)
router.register('customer-address', views.CustomerAddressViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
