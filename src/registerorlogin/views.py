from django.shortcuts import render
from registerorlogin.forms import UserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = UserForm()
    return render(request,'register.html',{'forms':forms})