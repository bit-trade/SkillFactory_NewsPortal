from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'subscribed')
    list_display_links = ('user_name',)


admin.site.register(Subscriber, SubscriberAdmin)

