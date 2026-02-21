from django import forms

class DocumentUploadForm(forms.Form):
    pinfl = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    desc = forms.CharField()