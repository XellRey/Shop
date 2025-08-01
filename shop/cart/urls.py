from django.urls import path

from cart.views import add_to_cart, remove, update, clear, cart_detail

urlpatterns = [
    path('product_add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_product/<int:product_id>/', remove, name='remove'),
    path('update/<int:product_id>/', update, name='update'),
    path('clear/', clear, name='clear'),
    path('detail/', cart_detail, name='cart_detail')
]