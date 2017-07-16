from django import forms
from .models import Contact

# connect the form to the model (database)
# need class Meta => link with model
class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = [
            'name',
            'email',
            'message',
        ]
