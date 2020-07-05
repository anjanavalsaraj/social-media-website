# Generated by Django 2.2.7 on 2020-06-19 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialite', '0003_auto_20200618_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=128)),
                ('mobile', models.CharField(max_length=12)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('place', models.CharField(choices=[('kerala', 'Kerala'), ('chennai', 'Chennai'), ('bangalore', 'Bangalore'), ('mysore', 'Mysore'), ('mumbai', 'Mumbai'), ('dubai', 'Dubai'), ('america', 'America')], max_length=128)),
                ('profession', models.CharField(blank=True, choices=[('softwareeng', 'Software engineer'), ('graphicdes', 'Graphic designer'), ('contentwriter', 'Content Writer'), ('senioracc', 'Senior accountant'), ('hr', 'HR Manager'), ('sales', 'Sales manager'), ('nurse', 'Nurse'), ('bde', 'Business development associate'), ('projectcord', 'Project co-ordinator'), ('flight', 'Flight attendant'), ('seo', 'Seo analyst'), ('student', 'Student')], max_length=128, null=True)),
                ('company', models.CharField(blank=True, choices=[('sbi', 'SBI'), ('wipro', 'Wipro'), ('accenture', 'Accenture'), ('byjus', 'Byjus'), ('max', 'Max Innovations'), ('hdfc', 'HDFC'), ('abc', 'ABC Corporation'), ('contract', 'Contracting plus'), ('techbyte', 'Techbyte technologies'), ('jet', 'Jet airways'), ('infosys', 'Infosys'), ('care+', 'Careplus hospital')], max_length=128, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]