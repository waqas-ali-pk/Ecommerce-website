from products.models import ProductCategory


def show_pages_menu(context):
    categories = ProductCategory.objects.all()
    pages_menu = [{'menu_title': category.category_name, 'product_category_id': category.product_category_id}
                  for category in categories]
    return {'pages_menu': pages_menu}
