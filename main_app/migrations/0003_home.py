# Generated by Django 5.0.4 on 2024-04-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_student_info_blood_student_info_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=100)),
                ('details', models.CharField(blank=True, max_length=230)),
                ('bg_image', models.ImageField(blank=True, upload_to='bg_image/%y')),
            ],
        ),
    ]
