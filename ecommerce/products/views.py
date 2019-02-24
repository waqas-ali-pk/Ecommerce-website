from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ProductCategory


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
