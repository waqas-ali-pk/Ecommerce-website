from products.models import ProductCategory


def show_pages_menu(context):
    categories = ProductCategory.objects.all()
    pages_menu = [{'menu_title': category.category_name, 'url': ''}
                  for category in categories]
    return {'pages_menu': pages_menu}
