from rest_framework import serializers
from .models import Customer, Fingerprint_device, Wallet, LED_bulb

class LED_bulbSerializer(serializers.ModelSerializer):
    model = LED_bulb
    fields = '__all__'