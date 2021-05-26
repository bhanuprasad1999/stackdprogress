from django.shortcuts import render,HttpResponseRedirect
from datetime import datetime

# Create your views here.
def progress(request,userid):
    context = []
    for i in range(1,32):
        context.append(i)
    return render(request,'progress.html',{'context':context,'userid':userid})

def daysheet(request):
    return render(request,'daysheet.html')

def pagenotfound(request):
    return render(request,'pagenotfound.html')