from django import forms
from datetime import datetime as dt

class ContentForm(forms.Form):

    topic = forms.CharField(max_length=100)

    subject = forms.CharField(max_length=20)

    summary = forms.Textarea()


choices = [('1','January'), ('2','February'), ('3','March'), ('4','April'), ('5','May'), ('6','June'), ('7','July'), ('8','August'), ('9','September'),('10','October'),('11','November'),('12','December')]

class DateForm(forms.Form):

    year = forms.IntegerField(max_value=3000,initial=dt.now().year, widget=forms.NumberInput(attrs={'onchange':'submit();'}),required=True)

    month = forms.ChoiceField(choices=choices,initial=dt.now().month, widget=forms.Select(attrs={'onchange':'submit();'}))
    
