from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cart.cart import CartManager
from order.forms import OrderCreateForm
from order.models import OrderItems


# Create your views here.

@login_required
def order_create(request):
    cart = CartManager(request.user)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid:
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price()
            order.save()

            for item in cart.items:
                OrderItems.objects.create(
                    order = order,
                    product = item['product'],
                    quantity = item['quantity'],
                    price = item['product'].price
                )

            cart.clear()
            return redirect("order_success", order_id=order.id)
    else:
        form = OrderCreateForm()

    data = {
        'cart': cart,
        'form': form
    }
    return render(request, 'order/create.html', data)

