from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LED_bulbList, LED_bulb_pd, Customer_UUID, Fingerprint_device_location, Mappingstation_price,Create_Transaction, Customer_status_uuid, Wallet_PP, Wallet_money, Fingerprint_device_status,Update_Transaction
from biometric_ticket import views


app_name = 'biometric_ticket'

urlpatterns = [
    path('ledbulb',  LED_bulbList.as_view(), name = 'ledbulb'),
    path('ledbulbpd',  LED_bulb_pd.as_view(), name = 'ledbulbpd'),
    path('ledbulblist', views.led_bulb_list, name = 'ledbulblist'),
    path('ledbulbdetails/<int:id>',views.led_bulb_detail, name = 'ledbulbdetails' ),
    # re_path(r'^(?P<id>)/?$',  LED_bulb_pd.as_view(), name = 'ledbulboption'),

    # Urls for Customer Api

    path('validateCustomer/<uuid>', Customer_UUID.as_view(), name = 'validateCustomer' ),

    # Urls for Fingerprint_device location
    path('fingerprintdevice/location', Fingerprint_device_location.as_view(), name = 'Fingerprint_device_location' ),


      # Urls for Fingerprint_device status
    path('fingerprintdevice/status', Fingerprint_device_status.as_view(), name = 'Fingerprint_device_status' ),
    
    # Urls for MappingStation api
    path('mappingstation_price/<source>/<destination>', Mappingstation_price.as_view(), name = 'Mappingstation_price'),

    #url for customer status and uuid
    path('customerstatus', Customer_status_uuid.as_view(), name = 'customerstatus' ), 
    #url for create transaction 
     path('transaction/create', Create_Transaction.as_view(), name = 'createtransaction' ),  


     #url for create transaction 
     path('transaction/update', Update_Transaction.as_view(), name = 'updatetransaction' ),   


    #url for fingerprint
    path('fingerprint',views.finger_html, name = 'abc'),

    path('wallet/<uuid>',Wallet_money.as_view(), name = 'wallet'),
    path('wallet_pp',Wallet_PP.as_view(), name = 'wallet'),





]
urlpatterns = format_suffix_patterns(urlpatterns)           