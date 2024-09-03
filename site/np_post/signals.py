from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from .mail_distribution import email_recipient, user_notification


@receiver(post_save, sender=Post)
def new_publication(sender, instance, created, **kwargs):
    if created:
        recipients = email_recipient(instance)
        user_notification(recipients, 'На портале - свежие публикации в категориях которые вам интересны')

