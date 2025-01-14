from urllib import request

from django.shortcuts import render


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, TemplateView, View, UpdateView
from django.contrib import messages

from catalog.models import Product
from .models import Blog

#
# # The class for rendering the Home page
# class HomeTemplateView(TemplateView):
#     template_name = 'catalog/home.html'

# The class for page with all blogs
class BlogListView(ListView):
    model = Blog


# The class for viewing page for particular Blog
class BlogDetailView(DetailView):
    model = Blog


# The class for viewing page for creating Blog
class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'picture']
    # name = request.POST.get('name')
    # messages.success(request, f'Thanks, message submitted successfully.')
    success_url = reverse_lazy('blog:blog_list')

# The class for viewing page for updating Blog
class BookUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'picture']
    # success_url = reverse_lazy('blog:blog_list')

    def post(self, request):
        """ Returns html file with contacts page and confirm that message was sent successfully """
        name = request.POST.get('name')
        messages.success(self.request, f'Thanks, {name}, message submitted successfully.')
        return redirect('blog:blog_list')

# # The class for creating Contacts page
# class ContactsTemplateView(View):
#     template_name = 'catalog/contacts.html'
#
#     def get(self, request):
#         """ Returns html file with contacts page and contacts list"""
#         contacts_company = Contact.objects.all()
#         return render(self.request, 'catalog/contacts.html', {'contacts_company': contacts_company})
#
#
#     def post(self, request):
#         """ Returns html file with contacts page and confirm that message was sent successfully """
#         name = request.POST.get('name')
#         messages.success(self.request, f'Thanks, {name}, message submitted successfully.')
#         return redirect('home:contacts_template')
