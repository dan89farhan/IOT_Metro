from django.shortcuts import render

from django.http import HttpResponse, Http404

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics, permissions, status
from rest_framework.parsers import JSONParser
from .models import LED_bulb, Customer, Fingerprint_device, Mappingstation
from rest_framework.decorators import api_view


# for LED Buld only
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LED_bulbSerializer, CustomerSerializer, Fingerprint_deviceSerializer, MappingstationSerializer

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

class LED_bulb_pd(APIView):
    
    def get_object(self, id):
        try:
            return LED_bulb.objects.get(id = id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, format = None):
        id = request.data.get('id')
        led_bulb = self.get_object(id)
        serializer = LED_bulbSerializer(led_bulb)
        return Response(serializer.data)

    def put(self, request, format = None):
        # print("Type is ", type(id), id, request.data.get('id') )
        id = request.data.get('id')
        led_bulb =self.get_object( id )
        serializer = LED_bulbSerializer(led_bulb, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, format = None):
        id = request.data.get('id')
        led_bulb = self.get_object(id)
        led_bulb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Customer get UUID

class Customer_UUID(APIView):

    def get_object(self, uuid):
        try:
            return Customer.objects.get(uuid = uuid)
        except ObjectDoesNotExist:
            raise Http404
    
    def get(self, request, uuid, format = None):
        # uuid = request.data.get('uuid')
        customer = self.get_object(uuid)
        serializer = CustomerSerializer(customer, many = False)
        # print(serializer.data['uuid'])
        return Response(serializer.data['uuid'], status = status.HTTP_200_OK)


# Fingerprint_device get Location

class Fingerprint_device_location(APIView):
    def get_object(self, fid):
        try:
            return Fingerprint_device.objects.get(fid = fid)
        except ObjectDoesNotExist:
            raise Http404
    
    def get(self, request, fid, format = None):
        
        location = self.get_object(fid)
        serializer = Fingerprint_deviceSerializer(location, many = False)
        
        return Response(serializer.data['location'], status = status.HTTP_200_OK)



# Mappingstation get price

class Mappingstation_price(APIView):
    def get_object(self, source, destination):
        try:
            return Mappingstation.objects.defer(destination).filter(all_station_name = source)
            # .values('ghatkopar')
            # return Mappingstation.objects.all()
        except ObjectDoesNotExist:
            raise Http404
    
    def get(self, request, source, destination, format = None):
        
        # print("Line 120 ",source, destination)
        price = self.get_object(source, destination)
        
        serializer = MappingstationSerializer(price, many = True)
        print(serializer.data[0][destination])
        
        return Response(serializer.data[0][destination], status = status.HTTP_200_OK)








@api_view(['GET', 'POST'])
def led_bulb_list(request, format = None):
    if request.method == 'GET':
        led_bulb = LED_bulb.objects.all()
        serializer = LED_bulbSerializer(led_bulb, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = JSONParser.parse(request.data)
        data = request.data
        serializer = LED_bulbSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def led_bulb_detail(request, id, format = None):
    try:
        led_bulb = LED_bulb.objects.get(id = id)
    except led_bulb.DeosNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LED_bulbSerializer(led_bulb)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LED_bulbSerializer(led_bulb, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        led_bulb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

class Transaction_uuid(APIView):
    def get_object(self, uuid):
        try:
            return Transaction_uuid.objects.get(uuid = uuid)
        except ObjectDoesNotExist:
            raise Http404
    
    def get(self, request, uuid, format = None):
        
        Transaction = self.get_object(uuid)
        serializer = Fingerprint_deviceSerializer(Transaction, many = False)
        
        return Response(serializer.data['location'], status = status.HTTP_200_OK)
