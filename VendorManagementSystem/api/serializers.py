from rest_framework import serializers
from .models import *

       
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields="__all__"
        
class VendorSerializer(serializers.ModelSerializer):
    Purchase_Order=PurchaseOrderSerializer(many=True, read_only=True)
    class Meta:
        model=Vendor
        fields="__all__"