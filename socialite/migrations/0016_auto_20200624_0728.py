# Generated by Django 2.2.7 on 2020-06-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialite', '0015_auto_20200624_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content2',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]