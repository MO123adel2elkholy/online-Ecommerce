from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.v

def all_products(request):
    all_p = Product.objects.all()
    paginator = Paginator(all_p, 4)  # Show 25 contacts per page //
    page = request.GET.get("page")
    all_p = paginator.get_page(page)
    Context = {'all_products': all_p}
    return render(request, 'product/products.html', Context)



def one_product(request, slug):

    Context={"one_pro":Product.objects.get(proslug=slug)}

    return render(request, 'product/product.html', Context)

