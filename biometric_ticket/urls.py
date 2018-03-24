from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LED_bulbList

urlpatterns = [
    path('ledbulb',  LED_bulbList.as_view(), name = 'ledbulb')
]
urlpatterns = format_suffix_patterns(urlpatterns)