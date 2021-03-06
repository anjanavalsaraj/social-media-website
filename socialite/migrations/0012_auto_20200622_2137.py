# Generated by Django 2.2.7 on 2020-06-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialite', '0011_auto_20200622_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='company',
            field=models.CharField(blank=True, choices=[('SBI', 'SBI'), ('Wipro', 'Wipro'), ('Accenture', 'Accenture'), ('Byjus', 'Byjus'), ('Max Innovations', 'Max Innovations'), ('HDFC', 'HDFC'), ('ABC Corporation', 'ABC Corporation'), ('Contracting plus', 'Contracting plus'), ('Techbyte technologies', 'Techbyte technologies'), ('Jet airways', 'Jet airways'), ('Infosys', 'Infosys'), ('Careplus hospital', 'Careplus hospital')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profession',
            field=models.CharField(blank=True, choices=[('Software engineer', 'Software engineer'), ('Graphic designer', 'Graphic designer'), ('Content Writer', 'Content Writer'), ('Senior accountant', 'Senior accountant'), ('HR Manager', 'HR Manager'), ('Sales manager', 'Sales manager'), ('Nurse', 'Nurse'), ('Business development associate', 'Business development associate'), ('Project co-ordinator', 'Project co-ordinator'), ('Flight attendant', 'Flight attendant'), ('Seo analyst', 'Seo analyst'), ('Student', 'Student')], max_length=128, null=True),
        ),
    ]
