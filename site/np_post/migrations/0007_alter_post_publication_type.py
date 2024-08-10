# Generated by Django 5.0.6 on 2024-08-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np_post', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_type',
            field=models.CharField(choices=[('новость', 'Новость'), ('статья', 'Статья')], default='новость', max_length=8),
        ),
    ]