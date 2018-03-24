from django.shortcuts import render

from django.http import HttpResponse

from rest_framework import generics, permissions, status
from rest_framework.parsers import JSONParser
from .models import LED_bulb



# for LED Buld only
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LED_bulbSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class LED_bulbList(APIView):
    def get(self, request, format = None):
        led_bulb = LED_bulb.objects.all()
        serializer = LED_bulbSerializer(led_bulb, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        
        # data = JSONParser().parse(request)
        
        
        # print('date ',led_bulb)
        serializer = LED_bulbSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id, format = None):
        led_bulb = LED_bulb.objects.get(id = id)
        serializer = LED_bulbSerializer(led_bulb, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format = None):
        led_bulb = LED_bulb.objects.get(id = id)
        led_bulb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)