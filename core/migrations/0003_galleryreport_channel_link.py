# Generated by Django 5.1.1 on 2024-10-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_report_galleryreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryreport',
            name='channel_link',
            field=models.URLField(default='http://youtube.com'),
        ),
    ]
