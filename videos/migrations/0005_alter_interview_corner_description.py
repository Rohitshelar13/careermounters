# Generated by Django 4.0.2 on 2022-04-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_apptitude_video_companyname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview_corner',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
