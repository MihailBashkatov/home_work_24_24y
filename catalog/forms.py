from django import forms
from django.core.exceptions import ValidationError

from .models import Product

""" List of prohibited words"""
PROHIBITED_WORDS = ['bes', 'tol']

#Creating class ModelForm for adding product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'product_image', 'category', 'product_price']

    #Validator against word in PROHIBITED WORDS list in the name of the product or in the description
    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        product_description = cleaned_data.get('product_description')
        for word in PROHIBITED_WORDS:
            if word in product_name or word in product_description:
                raise ValidationError(f"Word {word} is not possible to use nor in Product name neither in description")

        return cleaned_data

#     def __init__(self, *args, **kwargs):
#         super(AuthorForm, self).__init__(*args, **kwargs)
#
#         self.fields['first_name'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Insert First name'
#             })
#
#         self.fields['last_name'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Insert Last name'
#             })
#
#         self.fields['birth_date'].widget.attrs.update({
#             'class': 'form-control',
#             'type': 'date',
#             })
#
#     def clean(self):
#         cleaned_data = super().clean()
#         first_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')
#         if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
#             raise ValidationError("Author with such name already exists")
#         return cleaned_data
#
#
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'public_date', 'author']
#
#     def __init__(self, *args, **kwargs):
#         super(BookForm, self).__init__(*args, **kwargs)
#
#         self.fields['title'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Insert Book name'
#             })
#
#         self.fields['public_date'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Insert Date of publication'
#             })
#         self.fields['author'].widget.attrs.update({
#             'class': 'form-control',
#             })
