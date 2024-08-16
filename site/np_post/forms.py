from django.core.mail import send_mail
from django import forms
from .models import Post, Category


class PublicForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text_post', 'author', 'category']

    # def sending_mail(self, user):
    #     send_mail(
    #         subject='',
    #         message='',
    #         from_email='',
    #         recipient_list=[],
    #     )
    #     self.cleaned_data['text_post'] = self.cleaned_data['text_post']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=30, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class SectionForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_cat', 'description']

