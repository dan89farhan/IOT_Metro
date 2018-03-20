from django.shortcuts import render

from django.http import HttpResponse

from rest_framework import generics, permission
from .models import LED_bulb

from .permissions import IsOwner

# for LED Buld only
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

