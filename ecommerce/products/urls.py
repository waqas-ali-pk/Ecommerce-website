from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'productcategories/$', views.ProductCategoryList.as_view(), name='productcategory_list'),
    url(r'productcategory/(?P<pk>[0-9]+)/$', views.ProductCategoryDetail.as_view(), name='productcategory_detail'),
    url(r'create/$', views.ProductCategoryCreate.as_view(), name='productcategory_create'),
    url(r'update/(?P<pk>[0-9]+)/$', views.ProductCategoryUpdate.as_view(), name='productcategory_update'),
    url(r'delete/(?P<pk>[0-9]+)/$', views.ProductCategoryDelete.as_view(success_url='/products/productcategories/'),
        name='productcategory_delete'),

]
