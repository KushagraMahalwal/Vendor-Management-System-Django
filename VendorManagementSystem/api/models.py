from django.db import models
import uuid

class Vendor(models.Model):
    name=models.CharField(max_length=200)
    contact_details=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    vendor_code= models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    # Fields
    po_number = models.CharField(max_length=50, unique=True, blank=True, null=True, editable=False)
    vendor_reference = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    items = models.TextField()  # You might consider a more specific field type depending on your data structure
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generate a unique PO number using UUID
        if not self.po_number:
            self.po_number = str(uuid.uuid4())[:8].upper()  # You can adjust the length and formatting as needed
        super().save(*args, **kwargs)

    def __str__(self):
        return self.po_number
