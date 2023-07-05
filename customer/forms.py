from django import forms

from .models import AddCustomer
...

class CustomerForm(forms.ModelForm):
   class Meta:
     model = AddCustomer()
     fields = '__all__'
