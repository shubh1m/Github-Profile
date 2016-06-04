from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter UserID here'}))