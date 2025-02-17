from .services import ProductService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    View,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

from .forms import ProductForm
from .models import Contact, Product, Category


# The class for the logic to unpublish a product
class ProductUnpublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden(
                "You do not have permission to unpublish this product"
            )

        product.product_is_published = False
        product.save()

        return redirect("catalog:products_list")


# The class for rendering the Home page
class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"


class CategoryListView(ListView):
    model = Category


class ChosenCategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/chosen_category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.object.id
        context['category_name'] = self.object.category_name
        context["chosen_products"] = ProductService.get_all_products_for_category(
            category_id
        )
        return context


# The class for page with all products. With decorator for cashes
@method_decorator(cache_page(60 * 2), name="dispatch")
class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        """Return only published products. If queryset is not cached, set cache_queryset"""
        cache_queryset = cache.get("products_queryset")
        if not cache_queryset:
            cache_queryset = super().get_queryset()
            cache.set("products_queryset", cache_queryset, 60 * 2)

        return cache_queryset.filter(product_is_published=True)


# The class for viewing page for particular product. With decorator for caches
@method_decorator(cache_page(60 * 2), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


# The class for viewing page with adding new Product
class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    # Automatically saving owner of he product
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# The class for viewing page with updating new Product
class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    # Adding logic to update product only for owner
    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


# The class for viewing page with deleting Product
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    # Adding logic to delete product only for owner or moderator
    def post(self, request, *args, **kwargs):
        user = self.request.user
        self.object = self.get_object()
        if user == self.object.owner or user.has_perm("catalog.delete_product"):
            return super().post(request, *args, **kwargs)
        raise PermissionDenied


# The class for creating Contacts page
class ContactsTemplateView(View):
    template_name = "catalog/contacts.html"

    def get(self, request):
        """Returns html file with contacts page and contacts list"""
        contacts_company = Contact.objects.all()
        return render(
            self.request,
            "catalog/contacts.html",
            {"contacts_company": contacts_company},
        )

    def post(self, request):
        """Returns html file with contacts page and confirm that message was sent successfully"""
        name = request.POST.get("name")
        messages.success(
            self.request, f"Thanks, {name}, message submitted successfully."
        )
        return redirect("home:contacts_template")
