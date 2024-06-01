from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse

def home(request):
     return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
   return render(request, 'pricing.html')

def contact(request):
   return render(request, 'contact.html')

def service_details(request):
   return render(request, 'service-details.html')


def get_a_quote(request):
   return render(request, 'get-a-quote.html')



