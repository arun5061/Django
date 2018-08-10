from django import forms

class todoform(forms.Form):
    text = forms.CharField(max_length=20, widget=forms.TextInput(
    attrs={'placeholder':'Enter todo item'}
    ))
