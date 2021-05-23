from django import forms
from django.forms.widgets import PasswordInput
import re

class UserForm(forms.Form):
    userid = forms.CharField(max_length=10)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    password = forms.CharField(min_length=8,max_length=10,widget=forms.PasswordInput())
    repassword = forms.CharField(min_length=8,max_length=10,widget=forms.PasswordInput())

    def clean_userid(self):
        userid = self.cleaned_data.get('userid')

        if userid == 'hello':
            raise forms.ValidationError('we have done two validation calls')

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if re.match('[a-zA-Z0-9]\w*@_\w+[a-zA-Z0-9]\w*',password) == None:                      #password verify example 
            raise forms.ValidationError('password consists of above symbols')