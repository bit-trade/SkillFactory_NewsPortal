from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django import forms
from .models import Post, Category
from news_portal.secret import mail_user
from .tasks import clear_list


class PublicForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text_post', 'author', 'category']

    def send_email(self):
        recipient_list = []
        for c in self.cleaned_data['category'].all():
            for u in c.user.all():
                recipient_list.append(u.email)

        html_content = render_to_string(template_name='send_new_post.html', context={'new_post': self.cleaned_data})
        msg = EmailMultiAlternatives(
            subject=f'{self.cleaned_data['title']} {self.cleaned_data['text_post']}',
            body=self.cleaned_data['text_post'],
            from_email=mail_user,
            to=clear_list(recipient_list),
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=30, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class SectionForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_cat', 'description']

