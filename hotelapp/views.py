from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .models import *
from .serializers import *


# Create your views here.

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset =Customer.objects.all()


class HotelViewSet(ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class WaiterViewSet(ModelViewSet):
    serializer_class = WaiterSerializer
    queryset = Waiter.objects.all()


class MenuViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()