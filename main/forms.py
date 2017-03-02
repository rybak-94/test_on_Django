from django import forms
from .models import Post
from .models import Test
from django.contrib.auth import authenticate

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title')



class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('author', 'title')



class LoginForm(forms.Form):
    username = forms.CharField(label=u'Username')
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None