from django.shortcuts import render, redirect
from django.forms import Form
from django.core import paginator
from .forms import MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q


# Products Parts Starts Here

def store(request):
    product = Paginator(Product.objects.all(), 6)
    page_number = request.GET.get("page")
    final_products = product.get_page(page_number)
    return render(request, 'store/store.html', {"products":final_products})


def search(request):
    if request.method == "POST":
        searched_for = request.POST["search"]
        searched_data = Product.objects.filter(Q(title__contains = searched_for) | Q(description__contains = searched_for))
        print(searched_data)
        return render(request, 'store/search.html',{"products":searched_data})
    else:
        return render(request, 'store/search.html')



# User Part Starts Here
def register(request):
    print(request)
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered")
    return render(request, 'store/register.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = email, password=password)

        if user != None:
            login(request, user)
            return redirect('store')
        else:
            messages.warning(request, "Email or Password Doesn't Matching")
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('store')

def product_details(request):
    return render(request, 'store/productdetails.html')