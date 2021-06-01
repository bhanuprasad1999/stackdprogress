from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime as dt
from .forms import DateForm
from calendar import monthrange

def progress(request,userid,day):
    if request.method == 'POST':
        forms = DateForm(request.POST)

        if forms.is_valid():

            year = forms.cleaned_data['year']
            month = forms.cleaned_data['month']
            # Since monthrange() is returning the tuple of (day,no.of days)
            daydate = list(monthrange(year, int(month)))
            days = range(1, daydate[1]+1)

    else:
        year = dt.now().year
        month = dt.now().month
        # Since monthrange() is returning the tuple of (day,no.of days)
        daydate = list(monthrange(year, int(month)))
        days = range(1, daydate[1]+1)
        forms = DateForm()
    return render(request,'progress.html',{'forms':forms,'year':year,'month':month,'days':days,'userid':userid})

