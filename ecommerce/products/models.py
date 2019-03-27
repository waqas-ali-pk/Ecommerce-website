from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType


class ProductCategory(models.Model):
    product_category_id = models.BigAutoField(primary_key=True)
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
    product_sub_category_id = models.BigAutoField(primary_key=True)
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
    product_id = models.BigAutoField(primary_key=True)
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
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=50, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class ProductAttributes(models.Model):
    product_attribute_id = models.BigAutoField(primary_key=True)
    attribute_id = models.ForeignKey(CustomAttributes)
    product_id = models.ForeignKey(Product)
    attribute_value = models.CharField(max_length=200, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class ProductReview(models.Model):
    product_review_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product)
    review_value = models.CharField(max_length=10, blank=False)
    review_comment = models.CharField(max_length=200, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class PaymentMethods(models.Model):
    payment_method_id = models.BigAutoField(primary_key=True)
    payment_method_name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)
    created_on = models.DateField(blank=False)
    created_user_id = models.IntegerField(blank=False)
    modified_on = models.DateField(null=True, blank=True)
    modified_user_id = models.IntegerField(null=True, blank=True)


class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __str__(self):
        return str(self.creation_date)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __str__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)
