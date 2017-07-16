from django import forms

class JoinForm(forms.Form):
    Email = forms.EmailField(label="Enter your mail")
    Username = forms.CharField(label="Enter your name", max_length=250)
