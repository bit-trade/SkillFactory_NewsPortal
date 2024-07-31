from django import forms
from .models import Post


class PublicForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text_post', 'author']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=30, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


