from django.contrib import admin

from .models import Cars, Drivers, Shipments, Customers 


admin.site.register(Cars)
admin.site.register(Drivers)
admin.site.register(Shipments)
admin.site.register(Customers)