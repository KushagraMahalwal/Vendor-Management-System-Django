from django.db import models

# Vendor Model
class Vendor(models.Model):
    name=models.CharField(max_length=50)
    contact_details=models.TextField(max_length=200)
    address=models.TextField(max_length=200)
    vendor_code= models.CharField(max_length=100)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

    # Names of vendor
    def __str__(self):
        return self.name
    
# Purchase Order Model
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE, related_name='Purchase_Order')
    order_date = models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField()
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField(null =True) 

    def __str__(self):
        return self.po_number
    
# Performance Evaluation
class PerformanceRecord(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="performance_records")
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
