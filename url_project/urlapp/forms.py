from django import forms
from .models import UrlModel


class UrlForm(forms.ModelForm):
    l_url = forms.CharField()

    class Meta:
        model = UrlModel
        fields = ['l_url']
