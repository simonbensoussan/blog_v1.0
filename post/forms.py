from django import forms
from .models import Post

# connect the form to the model (database)
# need class Meta => link with model
class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = [
            'title',
            'content',
            'image',
        ]
