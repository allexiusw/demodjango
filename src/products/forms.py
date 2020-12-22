from django import forms
from django.forms import widgets 

from .models import Product 

class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            if 'user_id' in kwargs['initial']:
                self.fields['user'].initial = kwargs['initila']['user_id']
