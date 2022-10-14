from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def get_home(request):
   return HttpResponse("<h1>Welcome</h1>") 

def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
      "product": {
         "name":product.name,
          "description": product.description,
           "price": product.price
      },
      }
    return render(request, "product_detail.html", context)

def get_products(request):
   products = Product.objects.all()
   product_list = []
   for product in products:
      product_list.append({
            "name": product.name,
            "price": f"{product.price} KD",
            "description": product.description
            })
   context = {"products": product_list}
   return render(request, "product-list.html", context)
