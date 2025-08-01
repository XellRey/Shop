from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cart.cart import CartManager
from order.forms import OrderCreateForm
from order.models import OrderItems


# Create your views here.

@login_required
def order_create(request):
    cart_manager = CartManager(request.user)
    cart = cart_manager.cart

    if request.method == 'POST':
        form = OrderCreateForm(request.POST, user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price()
            order.save()

            for item in cart.items.all():
                OrderItems.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )

            cart_manager.clear()
            return redirect("main" )
    else:
        form = OrderCreateForm(request.POST or None, user=request.user)

    return render(request, 'order/create.html', {'cart': cart, 'form': form})