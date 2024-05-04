from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .functions import *
from django.db.models import F
from django.db.models import Sum
from django.utils.timezone import make_aware
from django.utils import timezone
from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
# from rest_framework import generics


# vendor create/list View
class VendorCreate(APIView):
    # vender List
    def get(self,request):
        vendor=Vendor.objects.all()
        serializer=VendorSerializer(vendor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Vendor Create View
    def post(self,request):
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# vendor details View
class VendorDetails(APIView):
    # Fetching vendor acc. to id
    def get(self,request, pk):
        try:
            vendor=Vendor.objects.get(pk=pk)
        except:
            return Response({'error':'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Updating vendor info
    def put(self,request,pk):
        vendor=Vendor.objects.get(pk=pk)
        serializer=VendorSerializer(vendor,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting Vendor
    def delete(self,request,pk):
        try:
            vendor=Vendor.objects.get(pk=pk)
        except:
            return Response({"msg":"Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response({'data':'task deleted'}, status=status.HTTP_204_NO_CONTENT)


# Purchase Order View
class PurchaseOrderCreate(APIView):
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['vendor__name']
    # List PO's
    def get(self,request):
        order=PurchaseOrder.objects.all()
        serializer=PurchaseOrderSerializer(order, many=True)
        return Response(serializer.data)
    
    # Create PO
    def post(self, request):
        serializer=PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# PO Details view
class PurchaseOrderDetails(APIView):
     # List PO acc. to Id
    def get(self,request,pk):
        try:
            order=PurchaseOrder.objects.get(pk=pk)
        except:
            return Response({"msg":"No Purchase Order Found"})
        serializer=PurchaseOrderSerializer(order)
        return Response(serializer.data)
    
    # Update PO
    def put(self,request,pk):
        try:
            order=PurchaseOrder.objects.get(pk=pk)
        except:
            return Response({"msg":"No Purchase Order Found"})
        serializer=PurchaseOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Delete PO
    def delete(self,request,pk):
        try:
            order=PurchaseOrder.objects.get(pk=pk)
        except:
            return Response({"msg":"No Purchase Order Found"})
        order.delete()
        return Response({"msg":"Task Deleted"})
        

# Performance Record View
class PerformanceRecord(APIView):
     # Performance Record
    def get(self, request, pk):
        try:
            vendor = Vendor.objects.get(pk=pk)
            
            data = {
                'vendor_id': pk,
                'vendor_name':vendor.name,
                'on_time_delivery_rate':calculate_on_time_delivery_rate(vendor),
                'quality_rating_average': calculate_quality_rating_average(vendor),
                'average_response_time': calculate_average_response_time(vendor),
                'fulfillment_rate': calculate_fulfillment_rate(vendor),
            }
            return Response(data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    

# Acknowledgment PO View
class AcknowledgePurchaseOrder(APIView):
    def post(self, request, pk):
        # Retrieve the purchase order object
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)

        # Get the acknowledgment date from the request data
        acknowledgment_date_str = request.data.get('acknowledgment_date')
        if acknowledgment_date_str:
            try:
                # Parse the acknowledgment date string into a datetime object
                acknowledgment_date = timezone.datetime.strptime(acknowledgment_date_str, '%Y-%m-%d')
            except ValueError:
                return Response({'error': 'Invalid date format. Please provide the date in YYYY-MM-DD format.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Update the acknowledgment date
                purchase_order.acknowledgment_date = acknowledgment_date
                purchase_order.save()

                # Trigger recalculation of average_response_time (implement your logic here)

                return Response({'message': 'Purchase order acknowledged successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing acknowledgment_date parameter.'}, status=status.HTTP_400_BAD_REQUEST)

       