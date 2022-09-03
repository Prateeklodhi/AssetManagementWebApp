from pyexpat import model
from .models import Asset, Employee
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AssetForms(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        widgets = {
            'issue_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'purchase_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'asset_serial_number':forms.TextInput(attrs={'required': True}),
        } 
    

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            
        }

    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']