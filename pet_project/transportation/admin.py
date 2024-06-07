from django.contrib import admin

from .models import Cars, Drivers, Shipments, Customers, Quote, DestinationDrivers, Destinations


admin.site.register(Cars)
admin.site.register(Drivers)
admin.site.register(Shipments)
admin.site.register(Customers)
admin.site.register(Quote)
admin.site.register(DestinationDrivers)
admin.site.register(Destinations)

