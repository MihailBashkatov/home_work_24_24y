from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm
from .models import User


#Adding calls RegisterView for registration new users
class RegisterView(CreateView):
    model = User
    template_name = 'users/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')



    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)  # send welcome email
        return super().form_valid(form)

    def send_welcome_mail(self, user_mail):
        subject = 'Welcome to Catalog App!'
        message = 'Hello  thank you for joining our services!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_mail,]
        send_mail(subject, message, from_email, recipient_list)
