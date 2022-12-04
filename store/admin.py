from django.contrib import admin
from .models import User, Product

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "phone_number",
    ]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "price",
        "discounted_price"
    ]