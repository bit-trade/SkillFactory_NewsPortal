# Generated by Django 5.0.6 on 2024-08-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np_post', '0004_alter_author_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]