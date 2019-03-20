from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ProductCategory, ProductSubCategory, Product, ProductReview
from .forms import ProductReviewCreateForm, ProductCreateForm, \
    ProductUpdateForm, ProductCategoryCreateForm, ProductCategoryUpdateForm, \
    ProductSubCategoryCreateForm, ProductSubCategoryUpdateForm
from django.http import HttpResponseRedirect
import datetime


class ProductCategoryList(ListView):
    model = ProductCategory


class ProductCategoryDetail(DetailView):
    model = ProductCategory


class ProductCategoryCreate(CreateView):
    template_name = 'products/productcategory_form.html'
    form_class = ProductCategoryCreateForm

    def form_valid(self, form):
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = self.request.user.id
        product_category = form.save()
        product_category.save()
        return HttpResponseRedirect(product_category.get_absolute_url())


class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    template_name = 'products/productcategory_form.html'
    form_class = ProductCategoryUpdateForm

    def form_valid(self, form):
        product_category = form.save()
        product_category.modified_on = datetime.datetime.now()
        product_category.modified_user_id = self.request.user.id
        product_category.save()
        return HttpResponseRedirect(product_category.get_absolute_url())


class ProductCategoryDelete(DeleteView):
    model = ProductCategory


def search_product_category(request, product_category_id):
    all_products = Product.objects.filter(product_category_id=product_category_id)
    pc = ProductCategory.objects.get(product_category_id=product_category_id)
    page_title = pc.category_name
    return render(request, 'search_product_categories.html', {'allProducts':all_products, 'page_title':page_title})


class ProductSubCategoryList(ListView):
    model = ProductSubCategory


class ProductSubCategoryDetail(DetailView):
    model = ProductSubCategory


class ProductSubCategoryCreate(CreateView):
    template_name = 'products/productsubcategory_form.html'
    form_class = ProductSubCategoryCreateForm

    def form_valid(self, form):
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = self.request.user.id
        product_sub_category = form.save()
        product_sub_category.save()
        return HttpResponseRedirect(product_sub_category.get_absolute_url())


class ProductSubCategoryUpdate(UpdateView):
    model = ProductSubCategory
    template_name = 'products/productsubcategory_form.html'
    form_class = ProductSubCategoryUpdateForm

    def form_valid(self, form):
        product_sub_category = form.save()
        product_sub_category.modified_on = datetime.datetime.now()
        product_sub_category.modified_user_id = self.request.user.id
        product_sub_category.save()
        return HttpResponseRedirect(product_sub_category.get_absolute_url())


class ProductSubCategoryDelete(DeleteView):
    model = ProductSubCategory


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    template_name = 'products/product_form.html'
    form_class = ProductCreateForm

    def form_valid(self, form):
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = self.request.user.id
        product = form.save()
        product.save()
        return HttpResponseRedirect(product.get_absolute_url())


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    form_class = ProductUpdateForm

    def form_valid(self, form):
        product = form.save()
        product.modified_on = datetime.datetime.now()
        product.modified_user_id = self.request.user.id
        product.save()
        return HttpResponseRedirect(product.get_absolute_url())


class ProductDelete(DeleteView):
    model = Product


def buy_product_detail(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product_reviews = ProductReview.objects.filter(product_id=product_id)
    return render(request, 'products/buy_product_detail.html',
                  {'product': product, 'product_reviews': product_reviews})


class ProductReviewCreate(CreateView):
    template_name = 'products/add_product_review.html'
    form_class = ProductReviewCreateForm

    def form_valid(self, form):
        form.instance.product = Product.objects.get(product_id=self.kwargs['product_id'])
        form.instance.created_on = datetime.datetime.now()
        form.instance.created_user_id = self.request.user.id
        review = form.save()
        review.save()
        return HttpResponseRedirect(reverse_lazy('buy_product_detail', args=[review.product.product_id]))

    #
    # def get_success_url(self):
    #     return reverse('buy_product_detail', kwargs={'product_id': self.object.product_id.product_id})
    #
    # def get(self, request, *args, **kwargs):
    #     context = {'form': ProductReviewCreateForm()}
    #     return render(request, 'products/add_product_review.html', context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = ProductReviewCreateForm(request.POST)
    #     if form.is_valid():
    #         review = form.save()
    #         review.save()
    #         return HttpResponseRedirect(reverse_lazy('buy_product_detail', args=[review.product_id.product_id]))
    #     return render(request, 'products/add_product_review.html', {'form': form})
