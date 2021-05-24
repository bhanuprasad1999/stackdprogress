from django.shortcuts import render
from registerorlogin.forms import UserForm
from registerorlogin.models import UserModel
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def register(request):
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            userid = forms.cleaned_data['userid']
            firstname = forms.cleaned_data['firstname']
            print(firstname)
            lastname = forms.cleaned_data['lastname']
            password = forms.cleaned_data['password']
            password = make_password(password)
            usermodel = UserModel(None,userid, firstname, lastname, password)
            usermodel.save()
    else:
        forms = UserForm()
    return render(request,'register.html',{'forms':forms})