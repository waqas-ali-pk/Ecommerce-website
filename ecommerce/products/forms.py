from django import forms
from products.models import ProductReview, Product, ProductCategory


class ProductReviewCreateForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('review_value', 'review_comment')


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('product_id', 'created_on', 'created_user_id',
                   'modified_on', 'modified_user_id')


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('product_id', 'created_on', 'created_user_id',
                   'modified_on', 'modified_user_id')


class ProductCategoryCreateForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        exclude = ('product_category_id', 'created_on', 'created_user_id',
                   'modified_on', 'modified_user_id')


class ProductCategoryUpdateForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        exclude = ('product_category_id', 'created_on', 'created_user_id',
                   'modified_on', 'modified_user_id')
