from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

# def index(request):
#     return HttpResponse("Test API Platform")

class Create_machine(APIView):
    def post(self,request):
        return Response(status=status.HTTP_200_OK)
    def get(self,request):
        return Response(status=status.HTTP_200_OK)