from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ProductCategory, ProductSubCategory, Product


class ProductCategoryList(ListView):
    model = ProductCategory


class ProductCategoryDetail(DetailView):
    model = ProductCategory


class ProductCategoryCreate(CreateView):
    model = ProductCategory
    fields = '__all__'


class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    fields = '__all__'


class ProductCategoryDelete(DeleteView):
    model = ProductCategory


class ProductSubCategoryList(ListView):
    model = ProductSubCategory


class ProductSubCategoryDetail(DetailView):
    model = ProductSubCategory


class ProductSubCategoryCreate(CreateView):
    model = ProductSubCategory
    fields = '__all__'


class ProductSubCategoryUpdate(UpdateView):
    model = ProductSubCategory
    fields = '__all__'


class ProductSubCategoryDelete(DeleteView):
    model = ProductSubCategory


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'


class ProductDelete(DeleteView):
    model = Product
