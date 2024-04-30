from django.db import models
import uuid

class Vendor(models.Model):
    name=models.CharField(max_length=200)
    contact_details=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    vendor_code= models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)

    def __str__(self):
        return self.name