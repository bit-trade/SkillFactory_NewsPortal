from celery import shared_task
from datetime import timezone, datetime
from .models import Post
from .mail_distribution import email_recipient, clear_list, user_notification



@shared_task
def new_post():
    post = Post.objects.latest('date_creation')
    time_now = datetime.now(timezone.utc).timestamp()
    create_post = post.date_creation.timestamp()
    if time_now - create_post < 60.0:
        recipient_list = email_recipient(post)
        user_notification(recipient_list, 'Новые публикации в подписках ваших категорий')


@shared_task
def weekly_mailing():
    date_now = datetime.now(timezone.utc)
    posts = Post.objects.filter(
        date_creation__month=date_now.month,
        date_creation__day__gte=date_now.day - 7)
    recipient_list = []
    for p in posts:
        recipient_list += email_recipient(p)

    user_notification(recipients=clear_list(recipient_list),
                      message='Публикации портала за прошедшую неделю из подписок ваших категорий')

