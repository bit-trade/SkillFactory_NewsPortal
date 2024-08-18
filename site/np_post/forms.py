from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django import forms
from .models import Post, Category


class PublicForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text_post', 'author', 'category']

    def send_email(self):
        print(type(self.cleaned_data['category']), self.cleaned_data['category'], sep='\n\n')
        # html_content = render_to_string(template_name='send_new_post.html', context={'new_post': new_post,})
        # msg = EmailMultiAlternatives(
        #     subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
        #     body=appointment.message,
        #     from_email='peterbadson@yandex.ru',
        #     to=['skavik46111@gmail.com'],
        # )
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=30, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class SectionForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_cat', 'description']

