from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LED_bulbList, LED_bulb_pd, Customer_UUID, Fingerprint_device_location, Mappingstation_price
from biometric_ticket import views

urlpatterns = [
    path('ledbulb',  LED_bulbList.as_view(), name = 'ledbulb'),
    path('ledbulbpd',  LED_bulb_pd.as_view(), name = 'ledbulbpd'),
    path('ledbulblist', views.led_bulb_list, name = 'ledbulblist'),
    path('ledbulbdetails/<int:id>',views.led_bulb_detail, name = 'ledbulbdetails' ),
    # re_path(r'^(?P<id>)/?$',  LED_bulb_pd.as_view(), name = 'ledbulboption'),

    # Urls for Customer Api

    path('validateCustomer/<uuid>', Customer_UUID.as_view(), name = 'validateCustomer' ),

    # Urls for Fingerprint_device api
    path('Fingerprint_device_location/<fid>', Fingerprint_device_location.as_view(), name = 'Fingerprint_device_location' ),
    
    # Urls for MappingStation api
    path('Mappingstation_price/<source>/<destination>', Mappingstation_price.as_view(), name = 'Mappingstation_price'),
]
urlpatterns = format_suffix_patterns(urlpatterns)