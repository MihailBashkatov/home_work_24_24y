from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'phone_number', 'avatar']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-input", "placeholder": " Insert email"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Insert password"}
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control", "placeholder": "Repeat password"
            }
        )

        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Insert phone number"}
        )

        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Upload avatar"}
        )