from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from np_post.models import Category


class Subscriber(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subs_user')
    category = models.ManyToManyField(Category, blank=True, related_name='subs_category')

    def __str__(self):
        if self.subscribed:
            cat_list = []
            for category in self.category.all():
                cat_list.append(category.name_cat)

            return f'{self.user_name} подписан на категории: {", ".join(cat_list)}'

        return f'{self.user_name} подписку не оформлял'

    def get_absolute_url(self):
        return reverse('subs_detail', args=[str(self.id)])

