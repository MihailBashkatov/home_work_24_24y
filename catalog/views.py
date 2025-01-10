from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import CreateView, ListView, DetailView

from .models import Contact, Product


# The class for creating page with all products
class ProductsListView(ListView):
    model = Product


# The class for viewing page for particular product
class ProductDetailView(DetailView):
    model = Product




def home(request):
    """ Returns html file with main page"""
    return render(request, 'catalog/home.html')



def contacts(request):
    """ Return html file. In case in method POST, taking all needed data"""

    # Get all values for model Contact to add it in render
    contacts_company = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Data submitted, {name}')

    return render(request, 'catalog/contacts.html', {'contacts_company': contacts_company})



def index(request, product_id):
    """ Return html file for particular product (by product_id). If not image, then field changes to ..."""

    product = Product.objects.get(id=product_id)
    if not product.product_image:
        product.product_image = '...'
    context = {'product':product}
    return render(request, 'catalog/product_detail.html', context)

#
# def products_list(request):
#     """ Returns html file with list of the products page"""
#     products = Product.objects.all()
#     context = {'products':products}
#     return render(request, 'catalog/product_list.html', context)