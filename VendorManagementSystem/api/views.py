from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class VendorCreate(APIView):
    def get(self,request):
        vendor=Vendor.objects.all()
        serializer=VendorSerializer(vendor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
