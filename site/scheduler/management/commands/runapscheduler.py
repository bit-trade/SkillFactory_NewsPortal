import logging

from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from np_post.models import Category
from news_portal.secret import mail_user


logger = logging.getLogger(__name__)


def my_job():
    sections = Category.objects.all()
    for section in sections:
        post_list = []
        for post in section.post_category.all():
            post_list.append(post.title)

        recipients = []
        for user in section.user.all():
            recipients.append(user.email)

        html_content = render_to_string(template_name='scheduler/public_announc.html',
                                        context={'posts': post_list})
        msg = EmailMultiAlternatives(subject='Анонс публикаций за неделю в любимых категория портала',
                                     from_email=mail_user, to=recipients)
        msg.attach_alternative(html_content, "text/html")
        msg.send()


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = 'Runs apscheduler.'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')
        scheduler.add_job(my_job, trigger=CronTrigger(day_of_week='mon'), id='my_job', max_instances=1,
                          replace_existing=True)
        logger.info("Added job 'my_job'.")
        scheduler.add_job(delete_old_job_executions, trigger=CronTrigger(week='*/2', hour='00', minute='00'),
                          id='delete_old_job_executions', max_instances=1, replace_existing=True)
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
