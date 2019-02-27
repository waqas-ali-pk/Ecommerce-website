from django.db import models


class ProductCategory(models.Model):
    product_category_id = models.IntegerField(blank=False, primary_key=True)
    category_name = models.CharField(max_length=50, blank=True)
    category_description = models.CharField(max_length=100, blank=True)
    create_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(blank=True)
    modified_user_id = models.IntegerField(blank=True)

    def get_absolute_url(self):
        return u'/products/productcategory/%d' % self.product_category_id


class ProductSubCategory(models.Model):
    product_sub_category_id = models.IntegerField(blank=False, primary_key=True)
    sub_category_name = models.CharField(max_length=50, blank=True)
    sub_category_description = models.CharField(max_length=100, blank=True)
    create_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(blank=True)
    modified_user_id = models.IntegerField(blank=True)

    def get_absolute_url(self):
        return u'/products/productsubcategory/%d' % self.product_sub_category_id


class Product(models.Model):
    product_id = models.IntegerField(blank=False, primary_key=True)
    product_category_id = models.ForeignKey(ProductCategory)
    product_sub_category_id = models.ForeignKey(ProductSubCategory)
    product_name = models.CharField(max_length=70, blank=True)
    product_description = models.CharField(max_length=200, blank=True)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(blank=True)
    modified_user_id = models.IntegerField(blank=True)

    def get_absolute_url(self):
        return u'/products/product/%d' % self.product_id
