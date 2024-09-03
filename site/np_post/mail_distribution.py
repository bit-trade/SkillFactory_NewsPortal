from django.core.mail import send_mail
from news_portal.secret import mail_user


def email_recipient(post):
    recipient_list = []
    for c in post.category.all():
        for u in c.user.all():
            recipient_list.append(u.email)

    recip_list = clear_list(recipient_list)
    return recip_list


def clear_list(recip_ls):
    recip_ls.sort()
    for i, j in zip(range(len(recip_ls)), recip_ls):
        number_of_emails = recip_ls.count(recip_ls[i])
        if number_of_emails > 1:
            c = number_of_emails - 1
            while c > 0:
                recip_ls.remove(j)
                c -= 1

    return recip_ls


def user_notification(recipients: list, message: str):
    send_mail(message=message, from_email=mail_user, recipient_list=recipients)

