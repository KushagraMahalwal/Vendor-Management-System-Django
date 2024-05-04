from .serializers import *
from django.db.models import F
from django.db.models import Sum

# On Time Delivery Rate
def calculate_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date'))
    total_completed_pos = completed_pos.count()
    if total_completed_pos > 0:
        on_time_delivery_rate = (on_time_deliveries.count() / total_completed_pos) * 100
    else:
        on_time_delivery_rate = 0
    return on_time_delivery_rate

# Quality Rating Average
def calculate_quality_rating_average(vendor):
    completed_pos_with_rating = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    total_completed_pos = completed_pos_with_rating.count()
    if total_completed_pos > 0:
        quality_rating_sum = completed_pos_with_rating.aggregate(Sum('quality_rating'))['quality_rating__sum']
        quality_rating_average = quality_rating_sum / total_completed_pos
    else:
        quality_rating_average = 0
    return quality_rating_average

# Average Response Time
def calculate_average_response_time(vendor):
    completed_pos_with_acknowledgment = PurchaseOrder.objects.filter(vendor=vendor, status='completed', acknowledgment_date__isnull=False)
    total_completed_pos = completed_pos_with_acknowledgment.count()
    if total_completed_pos > 0:
        response_times = [ (po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_pos_with_acknowledgment ]

        average_response_time = sum(response_times) / total_completed_pos
    else:
        average_response_time = 0
    return average_response_time

# Fullfillment Rate
def calculate_fulfillment_rate(vendor):
    total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
    if total_pos > 0:
        successfully_fulfilled_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        fulfillment_rate = (successfully_fulfilled_pos / total_pos) * 100
    else:
        fulfillment_rate = 0
    return fulfillment_rate


