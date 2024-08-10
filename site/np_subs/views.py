from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Subscriber
from .forms import SubscriberForm


class Subscription(LoginRequiredMixin, DetailView):
    model = Subscriber
    template_name = 'np_subs/subscription.html'
    context_object_name = 'subs_detail'


class SubsCreate(LoginRequiredMixin, CreateView):
    form_class = SubscriberForm
    model = Subscriber
    template_name = 'np_subs/subs_edit.html'

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        subs = form.save(commit=False)
        subs.user_name = user.username
        subs.first_name = user.first_name
        subs.last_name = user.last_name
        subs.email = user.email
        subs.subscribed = True
        subs.user = user
        return super().form_valid(form)


class SubsUpdate(LoginRequiredMixin, UpdateView):
    form_class = SubscriberForm
    model = Subscriber
    template_name = 'np_subs/subs_edit.html'

