from django.db import models
from .manager import UserManeger
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    is_phone_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManeger()

    def __str__(self):
        return self.username


CATEGORY_CHOICES = (
    ("Electronics", "Electronics"),
    ("Clothing", "Clothing"),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    discounted_price = models.FloatField()
    brand = models.CharField(max_length=50, default='ShopX')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    product_image = models.ImageField()

