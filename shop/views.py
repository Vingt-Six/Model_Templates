from django.shortcuts import render
from .models import Product

# Create your views here.
def homeproduct(request):
    products = Product.objects.all()
    return render(request, 'intromodel/product.html', {"products": products})