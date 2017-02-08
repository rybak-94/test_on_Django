from django import forms
from .models import Post
from .models import Test
from .models import ExtendUser

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title')



class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['author', 'title', 'type_user']


class UserForm(forms.ModelForm):

	class Meta:
		model = ExtendUser
		fields = ('type_user', 'age', 'name', 'city')

