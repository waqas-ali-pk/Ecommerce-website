from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    product_category_id = models.IntegerField(blank=False, primary_key=True)
    category_name = models.CharField(max_length=50, blank=True)
    category_description = models.CharField(max_length=100, blank=True)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return u'/products/productcategory/%d' % self.product_category_id


class ProductSubCategory(models.Model):
    product_sub_category_id = models.IntegerField(blank=False, primary_key=True)
    product_category = models.ForeignKey(ProductCategory)
    sub_category_name = models.CharField(max_length=50, blank=True)
    sub_category_description = models.CharField(max_length=100, blank=True)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sub_category_name

    def get_absolute_url(self):
        return u'/products/productsubcategory/%d' % self.product_sub_category_id


class Product(models.Model):
    product_id = models.IntegerField(blank=False, primary_key=True)
    product_category = models.ForeignKey(ProductCategory)
    product_sub_category = models.ForeignKey(ProductSubCategory)
    product_name = models.CharField(max_length=70, blank=True)
    product_description = models.CharField(max_length=200, blank=True)
    product_image = models.ImageField(upload_to='product_image', blank=True)
    p_price = models.DecimalField(blank=False, max_digits=11, decimal_places=2)
    s_price = models.DecimalField(blank=False, max_digits=11, decimal_places=2)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return u'/products/product/%d' % self.product_id


class CustomAttributes(models.Model):
    attribute_id = models.IntegerField(blank=False, primary_key=True)
    attribute_name = models.CharField(max_length=50, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class ProductAttributes(models.Model):
    product_attribute_id = models.IntegerField(blank=False, primary_key=True)
    attribute_id = models.ForeignKey(CustomAttributes)
    product_id = models.ForeignKey(Product)
    attribute_value = models.CharField(max_length=200, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class ProductReview(models.Model):
    product_review_id = models.IntegerField(blank=False, primary_key=True)
    product = models.ForeignKey(Product)
    review_value = models.CharField(max_length=10, blank=False)
    review_comment = models.CharField(max_length=200, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class PaymentMethods(models.Model):
    payment_method_id = models.IntegerField(blank=False, primary_key=True)
    payment_method_name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)
