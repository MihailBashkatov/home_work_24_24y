from catalog.models import Product


class ProductService:

    @staticmethod
    def get_all_products_for_category(category_id):
        """ Metod to get all products for particular category"""
        products = Product.objects.filter(category_id=category_id)
        return products
