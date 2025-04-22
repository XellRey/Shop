from django.shortcuts import render
from .models import Product
# Create your views here.

def main(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)