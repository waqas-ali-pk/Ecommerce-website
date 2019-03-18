from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'productcategories/$', views.ProductCategoryList.as_view(), name='productcategory_list'),
    url(r'productcategory/(?P<pk>[0-9]+)/$', views.ProductCategoryDetail.as_view(), name='productcategory_detail'),
    url(r'productcategory_create/$', views.ProductCategoryCreate.as_view(), name='productcategory_create'),
    url(r'productcategory_update/(?P<pk>[0-9]+)/$', views.ProductCategoryUpdate.as_view(),
        name='productcategory_update'),
    url(r'productcategory_delete/(?P<pk>[0-9]+)/$', views.ProductCategoryDelete.as_view(
        success_url='/products/productcategories/'), name='productcategory_delete'),

    url(r'search-product-categories/(?P<product_category_id>[0-9]+)/$', views.search_product_category,
        name='search-product-categories'),

    url(r'productsubcategories/$', views.ProductSubCategoryList.as_view(), name='productsubcategory_list'),
    url(r'productsubcategory/(?P<pk>[0-9]+)/$', views.ProductSubCategoryDetail.as_view(),
        name='productsubcategory_detail'),
    url(r'productsubcategory_create/$', views.ProductSubCategoryCreate.as_view(), name='productsubcategory_create'),
    url(r'productsubcategory_update/(?P<pk>[0-9]+)/$', views.ProductSubCategoryUpdate.as_view(),
        name='productsubcategory_update'),
    url(r'productsubcategory_delete/(?P<pk>[0-9]+)/$', views.ProductSubCategoryDelete.as_view(
        success_url='/products/productsubcategories/'), name='productsubcategory_delete'),

    url(r'products/$', views.ProductList.as_view(), name='product_list'),
    url(r'product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product_detail'),
    url(r'product_create/$', views.ProductCreate.as_view(), name='product_create'),
    url(r'product_update/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product_update'),
    url(r'product_delete/(?P<pk>[0-9]+)/$', views.ProductDelete.as_view(
        success_url='/products/products/'), name='product_delete'),

    url(r'buy_product_detail/(?P<product_id>[0-9]+)/$', views.buy_product_detail,
        name='buy_product_detail'),

    url(r'productreview_create/(?P<product_id>[0-9]+)/$', login_required(views.ProductReviewCreate.as_view()),
        name='productreview_create'),

]
