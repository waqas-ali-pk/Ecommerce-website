from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'productcategories/$', views.ProductCategoryList.as_view(), name='productcategory_list'),
    url(r'productcategory/(?P<pk>[0-9]+)/$', views.ProductCategoryDetail.as_view(), name='productcategory_detail'),
    url(r'productcategory_create/$', views.ProductCategoryCreate.as_view(), name='productcategory_create'),
    url(r'productcategory_update/(?P<pk>[0-9]+)/$', views.ProductCategoryUpdate.as_view(),
        name='productcategory_update'),
    url(r'productcategory_delete/(?P<pk>[0-9]+)/$', views.ProductCategoryDelete.as_view(
        success_url='/products/productcategories/'), name='productcategory_delete'),

    url(r'productsubcategories/$', views.ProductSubCategoryList.as_view(), name='productsubcategory_list'),
    url(r'productsubcategory/(?P<pk>[0-9]+)/$', views.ProductSubCategoryDetail.as_view(),
        name='productsubcategory_detail'),
    url(r'productsubcategory_create/$', views.ProductSubCategoryCreate.as_view(), name='productsubcategory_create'),
    url(r'productsubcategory_update/(?P<pk>[0-9]+)/$', views.ProductSubCategoryUpdate.as_view(),
        name='productsubcategory_update'),
    url(r'productsubcategory_delete/(?P<pk>[0-9]+)/$', views.ProductSubCategoryDelete.as_view(
        success_url='/products/productsubcategories/'), name='productsubcategory_delete'),

]
