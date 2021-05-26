from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from registerorlogin.forms import UserForm, LoginForm
from registerorlogin.models import UserModel
from django.contrib.auth.hashers import make_password

messages = {}
# Create your views here.
def register(request):
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            userid = forms.cleaned_data['userid']
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            password = forms.cleaned_data['password']
            password = make_password(password)
            if UserModel.objects.filter(userid=userid).exists() != True:
                usermodel = UserModel(None,userid, firstname, lastname, password)
                usermodel.save()
                return HttpResponseRedirect(reverse('login'))
                
    else:
        forms = UserForm()
    return render(request,'register.html',{'forms':forms,'messages':messages})



def login(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            userid = forms.cleaned_data['userid']
            return HttpResponseRedirect(reverse('progress',args=(userid,)))
    else:
        forms = LoginForm()
    return render(request,'login.html',{'forms':forms})
