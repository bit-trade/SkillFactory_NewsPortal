from celery import shared_task
from datetime import timezone, datetime, date
from django.core.mail import send_mail
from .models import Post
from news_portal.secret import mail_user


@shared_task
def new_post():
    post = Post.objects.latest('date_creation')
    time_now = datetime.now(timezone.utc).timestamp()
    create_post = post.date_creation.timestamp()
    recipient_list = []
    if time_now - create_post < 60.0:
        for c in post.category.all():
            for u in c.user.all():
                recipient_list.append(u.email)

        user_notification(clear_list(recipient_list), 'Новые публикации в подписках ваших категорий')


@shared_task
def weekly_mailing():
    date_now = datetime.now(timezone.utc)
    posts = Post.objects.filter(
        date_creation__month=date_now.month,
        date_creation__day__gte=date_now.day - 7)
    recipient_list = []
    for p in posts:
        for c in p.category.all():
            for u in c.user.all():
                recipient_list.append(u.email)

    user_notification(recipients=clear_list(recipient_list),
                      message='Публикации портала за прошедшую неделю из подписок ваших категорий')


def clear_list(recip_list):
    recip_list.sort()
    for i, j in zip(range(len(recip_list)), recip_list):
        number_of_emails = recip_list.count(recip_list[i])
        if number_of_emails > 1:
            c = number_of_emails - 1
            while c > 0:
                recip_list.remove(j)
                c -= 1

    return recip_list


def user_notification(recipients: list, message: str):
    send_mail(message=message, from_email=mail_user, recipient_list=recipients)

