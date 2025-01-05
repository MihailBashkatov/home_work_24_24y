from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from .models import Contact, Product

# Create your views here.


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
    return render(request, 'catalog/product.html', context)


def products_list(request):
    """ Returns html file with list of the products page"""
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'catalog/products_list.html', context)