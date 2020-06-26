from django import forms
from .models import Order

class AddCart(forms.Form):
    num_of_items = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self.max_count= kwargs.pop('max_count')

        super().__init__(*args, **kwargs)
        
        self.fields['num_of_items'].widget.attrs.update({
            'id':'inputColor', 
            'class':'form-control',
            'value':1,
            'autocomplete':'off', 
            'step': 1, 
            'min': 1,
            'max': self.max_count 
        })

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('firstname', 'lastname', 'phone', 'email', 'address', 'state', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class':'form-control','placeholder':'Your firstname'})
        self.fields['lastname'].widget.attrs.update({'class':'form-control','placeholder':'Your lastname'})
        self.fields['phone'].widget.attrs.update({'class':'form-control','placeholder':'Your Phone Number'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Your Email'})
        self.fields['address'].widget.attrs.update({'class':'form-control','placeholder':'Your Address'})
        self.fields['state'].widget.attrs.update({'class':'form-control','placeholder':'State'})
        self.fields['country'].widget.attrs.update({'class':'form-control','placeholder':'Country'})
        self.fields['city'].widget.attrs.update({'class':'form-control','placeholder':'Your City'})
     
