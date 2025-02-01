from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Blog


# The class for page with all blogs
class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        """ Return only published blogs.  """
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


# The class for viewing page for particular Blog
class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """"Return the amount of pages views."""

        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


# The class for viewing page for creating Blog
class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'picture']
    success_url = reverse_lazy('blog:blog_list')


# The class for viewing page for updating Blog
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'picture']
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        """Redirect to the blog detail page after successful update."""
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


# The class for viewing page for deleting Blog
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
