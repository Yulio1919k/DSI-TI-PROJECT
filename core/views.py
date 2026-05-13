from django.http import HttpResponse
from django.shortcuts import render
from portfolio.models import portfolio as port

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def portfolio_view(request):
    portfolio = port.objects.all()
    return render(request, 'core/portfolio.html', {'portfolio': portfolio})
