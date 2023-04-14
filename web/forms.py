# forms.py

from django import forms
from .models import Post

class addpostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',"author","status"]
