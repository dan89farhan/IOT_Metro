from rest_framework import serializers
from .models import Customer, Fingerprint_device, Wallet, LED_bulb, Mappingstation, Transaction

# LED Serializer For Api

class LED_bulbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LED_bulb
        fields = '__all__'    
        verbose_name = 'LED'
        verbose_name_plural = 'LEDs'


# Customer Serializer For Api    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('uuid', 'name')
        # fields = '__all__'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

# Fingerprint_device Serializer For Api    
class Fingerprint_deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint_device
        
        fields = '__all__'
        verbose_name = 'Fingerprint_device'
        verbose_name_plural = 'Fingerprint_devices'

# Mappingstation Serializer For Api

class MappingstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mappingstation
        
        fields = '__all__'
        verbose_name = 'Mappingstation'
        verbose_name_plural = 'Mappingstations'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction

        fields = ('uuid','source','destination','fare','status')
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'