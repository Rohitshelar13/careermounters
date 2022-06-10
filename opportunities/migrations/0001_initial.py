# Generated by Django 4.0.2 on 2022-04-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('companydescription', models.TextField(max_length=255)),
                ('perks', models.TextField(blank=True, max_length=255)),
                ('googleformlink', models.CharField(blank=True, max_length=255)),
                ('companywebsite', models.CharField(blank=True, max_length=255)),
                ('companyemail', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
