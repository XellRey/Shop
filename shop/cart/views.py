from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .cart import CartManager
from django.shortcuts import render
# Create your views here.

@login_required
def add_to_cart(request, product_id):
    cart = CartManager(request.user)
    cart.add_product(product_id)
    return redirect('cart_detail')


@login_required
def remove(request, product_id):
    cart = CartManager(request.user)
    cart.remove_product(product_id)
    return redirect('cart_detail')


@login_required
def clear(request):
    cart = CartManager(request.user)
    cart.clear()
    return redirect('cart_detail')


@login_required
def update(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            try:
                quantity = int(quantity)
                cart = CartManager(request.user)
                cart.update_quantity(product_id, quantity)
            except ValueError:
                pass
    return redirect('cart_detail')


def cart_detail(request):
    cart = CartManager(request.user)
    items = cart.cart.items.all()

    data = {
        'cart': cart,
        'items': items,
    }
    return render(request,'main/cart_detail.html', data)