from django.shortcuts import render, redirect
from .forms import QuoteForm, AuthUserRegistrationForm
from .models import Quote, AuthUser
from django.contrib import messages



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
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            quote_request = Quote.objects.create(
                departure=form_data['departure'],
                delivery=form_data['delivery'],
                weight=form_data['weight'],
                dimensions=form_data['dimensions'],
                name=form_data['name'],
                email=form_data['email'],
                phone=form_data['phone'],
                message=form_data['message']
            )
            
            return render(request, 'get-a-quote.html')
    else:
        form = QuoteForm()

    return render(request, 'get-a-quote.html')



def register(request):
    if request.method == 'POST':
        form = AuthUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Реєстрація успішна.')
            return redirect('home')  
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = AuthUserRegistrationForm()
    return render(request, 'register.html', {'form': form})


