# Generated by Django 2.2.7 on 2020-06-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialite', '0004_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
