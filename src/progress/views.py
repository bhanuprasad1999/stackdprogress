from django.shortcuts import render
from datetime import datetime as dt
from .forms import DateForm
from calendar import monthrange

# Create your views here.
def progress(request,userid):
    if request.method == 'POST':
        forms = DateForm(request.POST)

        if forms.is_valid():

            year = forms.cleaned_data['year']
            month = forms.cleaned_data['month']
            daydate = list(monthrange(year, int(month)))           # Since monthrange() is returning the tuple of (day,no.of days)
            days = range(1,daydate[1]+1)


    else:
        year = dt.now().year
        month = dt.now().month
        forms = DateForm()

    return render(request,'progress.html',{'forms':forms,'year':year,'month':month,'days':days})

