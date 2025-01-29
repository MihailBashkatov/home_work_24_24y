
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, TemplateView, View, UpdateView, DeleteView
from django.contrib import messages

from .forms import ProductForm
from .models import Contact, Product


# The class for rendering the Home page
class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

# The class for page with all products
class ProductsListView(ListView):
    model = Product


# The class for viewing page for particular product
class ProductDetailView(DetailView):
    model = Product

# The class for viewing page with adding new Product
class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

# The class for viewing page with updating new Product
class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

# The class for viewing page with deleting Product
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

# The class for creating Contacts page
class ContactsTemplateView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        """ Returns html file with contacts page and contacts list"""
        contacts_company = Contact.objects.all()
        return render(self.request, 'catalog/contacts.html', {'contacts_company': contacts_company})


    def post(self, request):
        """ Returns html file with contacts page and confirm that message was sent successfully """
        name = request.POST.get('name')
        messages.success(self.request, f'Thanks, {name}, message submitted successfully.')
        return redirect('home:contacts_template')

