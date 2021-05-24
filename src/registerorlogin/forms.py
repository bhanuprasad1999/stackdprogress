from django import forms
from django.forms.widgets import PasswordInput
import re

class UserForm(forms.Form):
    userid = forms.CharField(max_length=10)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    password = forms.CharField(min_length=8,max_length=10,widget=forms.PasswordInput())
    repassword = forms.CharField(min_length=8,max_length=10,widget=forms.PasswordInput())

    #UserId validation
    def clean_userid(self):
        userid = self.cleaned_data.get('userid')

        if re.match('[a-zA-Z0-9_]\w*@\w+[0-9]\w*',userid) == None:
            raise forms.ValidationError('The userid must be in format of alphabet and number@number only')
        return userid

    # Password Validation
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if re.match('[a-zA-Z0-9]\w*[@_!$?#]w*[a-zA-Z0-9]\w*',password) == None: 
            raise forms.ValidationError('The password must contain numbers and alphabets and some characters (@ _ ! ? $ #)')
        return password

    def clean_repassword(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password != repassword:
            raise forms.ValidationError('The password is not matched !')