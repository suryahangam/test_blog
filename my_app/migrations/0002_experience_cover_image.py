# Generated by Django 4.0.3 on 2022-03-20 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
