from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LED_bulbList, LED_bulb_pd
from biometric_ticket import views

urlpatterns = [
    path('ledbulb',  LED_bulbList.as_view(), name = 'ledbulb'),
    path('ledbulbpd/<int:id>',  LED_bulb_pd.as_view(), name = 'ledbulbpd'),
    path('ledbulblist', views.led_bulb_list, name = 'ledbulblist'),
    path('ledbulbdetails/<int:id>',views.led_bulb_detail, name = 'ledbulbdetails' ),
]
urlpatterns = format_suffix_patterns(urlpatterns)