# Generated by Django 3.0.4 on 2020-04-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runfit', '0002_auto_20200410_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='person_avatars/'),
        ),
    ]
