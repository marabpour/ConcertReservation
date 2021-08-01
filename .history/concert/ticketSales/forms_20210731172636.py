from django import forms
from ticketSales.models import ConcertModel

class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100,label="نام کنسرت",required=False)

class ConcertForm(forms.ModelForm):
    class Meta:
        model=
    