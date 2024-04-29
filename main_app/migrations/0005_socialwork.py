# Generated by Django 5.0.4 on 2024-04-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_home_bg_image_home_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='image/%y')),
                ('details', models.CharField(blank=True, max_length=230)),
            ],
        ),
    ]