# Generated by Django 5.0.6 on 2024-08-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np_post', '0007_alter_post_publication_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]