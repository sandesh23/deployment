from .models import *
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= Address
        fields ='__all__'


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer("address",many=True)
    class Meta:
        model = Customer
        fields = '__all__'



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields='__all__'


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Waiter
        fields='__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manager
        fields ='__all__'



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
