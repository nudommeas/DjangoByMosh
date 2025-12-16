from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True) #Automatically updates on each save

class Customer(models.Model):
    MEMBER_BRONZE = 'B'
    MEMBER_SILVER = 'S'
    MEMBER_GOLD = 'G'

    MEMBER_CHOICES= [
        (MEMBER_BRONZE, 'Bronze'),
        (MEMBER_SILVER, 'Silver'),
        (MEMBER_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True)
    phone = models.CharField()
    birth_data = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBER_CHOICES, default=MEMBER_BRONZE)

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