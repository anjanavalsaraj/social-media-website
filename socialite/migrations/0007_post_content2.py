# Generated by Django 2.2.7 on 2020-06-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialite', '0006_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=models.CharField(default='', max_length=100),
        ),
    ]
