from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, me_author, subs_me

urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('me_author/', me_author, name='me_author'),
    path('subs_me/<int:section_id>', subs_me, name='subs_me'),
]
