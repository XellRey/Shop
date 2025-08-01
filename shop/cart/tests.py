from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal

from .cart import CartManager
from .models import Cart, CartItem
from main.models import Product, Category

# Create your tests here.

class CartModelTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email ='testuser@test.com', password='testpass')
        self.cart = Cart.objects.create(user=self.user)
        self.category = Category.objects.create(name='Кофе')
        self.product = Product.objects.create(
            name='Кофе',
            price=Decimal('100.00'),
            category=self.category
        )

    def test_cart_item_total_price(self):

        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            price=Decimal('100.00'),
            quantity=2
        )
        self.assertEqual(item.total_price(), Decimal('200.00'))

    def test_cart_total_price(self):
        CartItem.objects.create(cart=self.cart, product=self.product, price=Decimal('100.00'), quantity=1)
        CartItem.objects.create(cart=self.cart, product=self.product, price=Decimal('50.00'), quantity=3)

        self.assertEqual(self.cart.total_price(), Decimal('250.00'))


class CartManagerTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email='testuser@test.com', password='testpass')

        self.category = Category.objects.create(name='Кофе')
        self.product1 = Product.objects.create(name='Латте', price=Decimal('100.00'), category=self.category)
        self.product2 = Product.objects.create(name='Раф', price=Decimal('50.00'), category=self.category)

        self.manager = CartManager(self.user)

    def test_add_product(self):
        self.manager.add_product(self.product1.id, quantity=5)
        items = CartItem.objects.filter(cart=self.manager.cart)

        self.assertEqual(items.count(), 1)
        self.assertEqual(items[0].quantity, 5)
