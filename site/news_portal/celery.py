import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

app = Celery('news_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending_new_publication': {
        'task': 'np_post.tasks.new_post',
        'schedule': 60,
    },
    'weekly_newsletter': {
        'task': 'np_post.tasks.weekly_mailing',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    }
}

