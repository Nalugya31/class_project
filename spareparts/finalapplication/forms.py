# forms for the workers to record sales
from django.forms import ModelForm
from .models import *
from django import forms
from .models import MyImage
#to add stock volume of a certain product.
# model of django to register users
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class AddForm(ModelForm):
    class Meta:
        model=Product
        fields=['received_quantity'] # received stock for workers to edit(incoming stock)


class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields=['quantity', 'amount_received','issued_to','contact','branch_name','part_name']

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ('title', 'image')