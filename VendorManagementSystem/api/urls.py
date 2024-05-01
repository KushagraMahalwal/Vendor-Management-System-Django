"""
URL configuration for VendorManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('vendor/', VendorCreate.as_view(), name="VendorCreate"),
    path('vendor/<int:pk>/', VendorDetails.as_view(), name="VendorDetails"),
    path('purchase_orders/', PurchaseOrderCreate.as_view(), name="PurchaseOrderCreate" ),
    path('purchase_orders/<int:pk>/',PurchaseOrderDetails.as_view(), name="PurchaseOrderDetails")
    
    ]
