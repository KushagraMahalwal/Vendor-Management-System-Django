from rest_framework import serializers
from .models import *

#Purchase Order    
class PurchaseOrderSerializer(serializers.ModelSerializer):
    # Added vendor name instead of id (Updated)
    # vendor_name=serializers.CharField(source='vendor.name', read_only=True)
    class Meta:
        model=PurchaseOrder
        fields="__all__"
        # exclude=('vendor',)
        

# Performance Evaluation
class PerformanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceRecord
        fields = "__all__"


# Vendor List
class VendorSerializer(serializers.ModelSerializer):
    Purchase_Order=PurchaseOrderSerializer(many=True, read_only=True)
    performance_records = PerformanceRecordSerializer(many=True, read_only=True)
    class Meta:
        model=Vendor
        fields="__all__"



