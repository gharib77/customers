from django import forms
from .models import Myuser

class AuthenticationForm(forms.Form): # Note: forms.Form NOT forms.ModelForm
    ut_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'ut_name','placeholder':'ut_name'}), 
        label='username')
    passuser = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'passuser','placeholder':'Password'}),
        label='Password')
    class Meta:
        fields = ['ut_name', 'passuser']