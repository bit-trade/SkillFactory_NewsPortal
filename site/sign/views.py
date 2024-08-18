from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import BaseRegisterForm
from np_post.models import Category


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def me_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

@login_required
def subs_me(request, section_id):
    user = request.user
    section = Category.objects.get(id=section_id)
    section.user.add(user)
    if not section.subscribed:
        section.subscribed = True

    return redirect('/authorization/')
