# Generated by Django 5.1 on 2024-12-21 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=400)),
                ('followers', models.CharField(max_length=400)),
                ('likes', models.CharField(max_length=400)),
                ('profile_picture', models.CharField(max_length=400)),
            ],
        ),
    ]
