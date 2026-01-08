from django.db import models
from django.core.validators import MinValueValidator
from django.contrib import admin
from django.conf import settings
import uuid
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True) #Automatically updates on each save
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')# collection is parent class
    promotion = models.ManyToManyField(Promotion)

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['title'] #sorting from A-Z alphabetically

class Customer(models.Model):
    MEMBER_BRONZE = 'B'
    MEMBER_SILVER = 'S'
    MEMBER_GOLD = 'G'

    MEMBER_CHOICES= [
        (MEMBER_BRONZE, 'Bronze'),
        (MEMBER_SILVER, 'Silver'),
        (MEMBER_GOLD, 'Gold')
    ]
    phone = models.CharField(max_length=100)
    birth_date = models.DateField()
    membership = models.CharField(max_length=1, choices=MEMBER_CHOICES, default=MEMBER_BRONZE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    # @admin.display(ordering='user__first_name') # used to sort a model fields
    # def first_name(self):
    #     return self.user.first_name
    # @admin.display(ordering='user__last_name')
    # def last_name(self):
    #     return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_STATUS_PENDING, 'PENDING'),
        (PAYMENT_STATUS_COMPLETED, 'COMPLETED'),
        (PAYMENT_STATUS_FAILED, 'FAILED')
    ]
    placed_at = models.DateTimeField(auto_now_add=True) #Automatically sets on creation
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #Primary key is not allowed to duplicate address
    #customer is the parent class

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']] # A product can only appear once in a given cart

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews') #In the product class, we'll have an attribute called reviews.
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)