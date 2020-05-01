# Generated by Django 3.0.4 on 2020-04-08 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('avatar', models.ImageField(upload_to='coach_avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('price', models.FloatField(default=0)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_type', to='runfit.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runfit.Coach')),
                ('training_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runfit.TypeOfTraining')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='person_avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('pick_training', models.IntegerField(choices=[(1, 'Фитнес'), (2, 'Аэробика'), (3, 'Гимнастика'), (4, 'Пилатес'), (5, 'Жиросжигание'), (6, 'Йога'), (7, 'Кроссфит'), (8, 'Спиннинг')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runfit.Coach')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runfit.Person')),
            ],
        ),
    ]