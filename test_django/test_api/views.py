from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.pyplot import cla
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from test_api.models import *



# Create your views here.

# def index(request):
#     return HttpResponse("Test API Platform")

class Create_machine(APIView):
    def post(self,request):
        try:
            machine_name=request.data['machine_name']
            marca=request.data['marca']
        
            Machines.objects.create(machine_name=machine_name, marca=marca)
        
            return Response({"response":"Registro agregado", "HasError":"False"},status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    def get(self,request):
        content={}
        list_machine=Machines.objects.all()
        
        raw_machine=[]
        for i in list_machine:
            dict_send={}
            dict_send["machine_name"]=i.machine_name
            dict_send["marca"]=i.marca
            dict_send["fecha de compra"]=i.buy_date
            raw_machine.append(dict_send)
        content["listado de maquinas"]=raw_machine
        
        return Response(content, status=status.HTTP_200_OK)

class Create_dots(APIView):
    def post(self, request):
        try:
            id_device = request.data['id_device']
            value = request.data['value']
            units = request.data['units']
            Dots.objects.create(devices_id = id_device, value= value, units= units)
            return Response({"Message": "Registro insertado", "HasError":"False"},status= status.HTTP_200_OK)
        except :
            return Response({"Message": "Something Wrong", "HasError":"True"},status= status.HTTP_501_NOT_IMPLEMENTED)
    
class Get_dots(APIView):
    def get(self,request,codigo):
        content={}
        list_dots=Dots.objects.filter(devices_id=codigo)
        
        raw_dots=[]
        for i in list_dots:
            dict_send={}
            dict_send["value"]=i.value
            dict_send["units"]=i.units
            
            raw_dots.append(dict_send)
        content["listado de puntos"]=raw_dots
        
        return Response(content, status=status.HTTP_200_OK)
    
    