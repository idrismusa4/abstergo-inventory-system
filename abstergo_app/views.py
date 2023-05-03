from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    return render(request, 'index.html')
def dashboard(request):
    products = Product.objects.all().order_by('-date_created')
    return render(request, 'dashboard.html',{'products':products})
def addprod(request):
    return render(request, 'addprod.html')
def editprod(request):
    return render(request, 'editprod.html')


