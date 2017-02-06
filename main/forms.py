from django import forms
from .models import Post
from .models import Test

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title')

class TestForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title')