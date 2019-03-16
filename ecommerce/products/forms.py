from django import forms
from products.models import ProductReview


class ProductReviewCreateForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('product_review_id', 'review_value',
                  'review_comment', 'created_on', 'created_user_id')
