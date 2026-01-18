from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def home(request):
    
    featured_products = Product.objects.filter(featured=True).order_by("-created_at")[:12]
    context = {
        "products": featured_products
    }
    
    return render(request, "store/home.html", context)

def products(request):
    
    products = Product.objects.all().order_by("-created_at")
    paginated_products = Paginator(products, 16)  # Show 16 products per page
    
    page_number = request.GET.get("page")
    page_obj = paginated_products.get_page(page_number)
    context = {
        "products": page_obj,
    }
    return render(request, "store/products.html", context)