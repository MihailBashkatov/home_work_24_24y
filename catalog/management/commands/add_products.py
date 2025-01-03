from unicodedata import category

from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):

        # Delete all products from database
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Creating Test Categor
        category, _ = Category.objects.get_or_create(category_name='Test product')

        # Preparing Test products for Test Category
        products = [
            {'product_name': 'test_1', 'product_description': 'test_description_1', 'category': category, 'product_price': '001'},
            {'product_name': 'test_2', 'product_description': 'test_description_2', 'category': category, 'product_price': '002'},
            {'product_name': 'test_3', 'product_description': 'test_description_3', 'category': category, 'product_price': '003'},
        ]

        # Adding Test Products to Test Category
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.product_name}'))