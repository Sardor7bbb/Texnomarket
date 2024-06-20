from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Qidiruv', max_length=100)