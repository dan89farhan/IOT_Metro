from django.contrib import admin
from .models import Customer, Fingerprint_device, Wallet, LED_bulb
# Register your models here.

admin.site.register(Customer)
admin.site.register(Fingerprint_device)
admin.site.register(Wallet)
# admin.site.register(LED_bulb)