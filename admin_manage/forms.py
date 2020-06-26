from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields =('name', 'description','price','image','stock',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Product Name'})
        self.fields['description'].widget.attrs.update({'class':'form-control','rows':2})
        self.fields['price'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Price'})
        self.fields['image'].widget.attrs.update({'class':'form-contorl', 'placeholder': 'Select Image'})
        self.fields['stock'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Stock'})
    