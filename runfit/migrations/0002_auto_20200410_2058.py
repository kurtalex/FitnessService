# Generated by Django 3.0.4 on 2020-04-10 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runfit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pick_training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runfit.TypeOfTraining'),
        ),
    ]
