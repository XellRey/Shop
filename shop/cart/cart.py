from .models import Cart, CartItem
from main.models import Product


class CartManager:


    def __init__(self, user):
        self.user = user
        self.cart, created = Cart.objects.get_or_create(user=user)


    def add_product(self, product_id, quantity=1):
        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(cart=self.cart, product=product)
            if not created:
                cart_item.quantity += quantity
            cart_item.save()
        except:
            pass


    def remove_product(self, product_id):
        CartItem.objects.filter(cart=self.cart, product_id=product_id).delete()


    def clear(self):
        self.cart.items.all().delete()


    def update_quantity(self, product_id, quantity):
        try:
            cart_item = CartItem.objects.get(cart=self.cart, product_id=product_id)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delet()
        except:
            pass