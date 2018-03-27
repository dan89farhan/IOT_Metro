from rest_framework import serializers
from .models import Customer, Fingerprint_device, Wallet, LED_bulb

class LED_bulbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LED_bulb
        fields = '__all__'    
        verbose_name = 'LED'
        verbose_name_plural = 'LEDs'
    