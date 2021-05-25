from django.shortcuts import render
from django.http import HttpResponse
from eshop.models import *

# Create your views here.
def  process_products(request):

    if request.method =='POST':
        item = request.POST.get("item")
        p = Product.objects.get(id=item)
        qty = request.POST.get("qty")
        data = {"order": f'{qty}x {p.name} ordered', "price": f"Total price: €{p.price * int(qty)}"}
        return render(request, "shop/confirmation.html", context=data)

    if request.method == 'POST':
        categories = ["Clothes", "Food", "Toys", "Computer", "Shoes"]
        shopname = "Cool Shop"
        products = Product.objects.all()
        contextdata = {"categories": categories,
                       "shopname": shopname,
                       "products": products}

        return render(request, "eshop/index.html", context=contextdata)

def  process_services(request):

    categories = ["Clothes", "Food", "Toys", "Computer", "Shoes"]
    shopname = "Cool Shop"
    contextdata = {"categories": categories,
                   "shopname": shopname}

    return render(request, "eshop/services.html", context=contextdata)

def  process_shop_main_page(request):
    return HttpResponse("welcome to the grand shop.")