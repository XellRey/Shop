from django.shortcuts import render
from unicodedata import category

from order.models import Order, OrderItems
from .models import Product, Category


# Create your views here.

def main(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)


def pizza(request):
    products = Product.objects.filter(category=3)
    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)


def coffe(request):
    products = Product.objects.filter(category=1)
    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)


def drinks(request):
    products = Product.objects.filter(category=2)
    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)


def desserts(request):
    products = Product.objects.filter(category=4)
    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)


def sauce(request):
    products = Product.objects.filter(category=5)
    data = {
        'products': products,
    }
    return render(request, 'main/index.html', data)


def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/profile.html',
                  {'orders': orders})