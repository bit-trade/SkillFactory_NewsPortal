# Generated by Django 5.0.6 on 2024-08-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np_post', '0005_alter_comment_rating_alter_post_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='post_category', to='np_post.category'),
        ),
    ]
