# Generated by Django 3.0.4 on 2020-04-13 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runfit', '0004_auto_20200410_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name': 'Тренер', 'verbose_name_plural': 'Тренеры'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='trainingschedule',
            options={'verbose_name': 'Рассписание', 'verbose_name_plural': 'Рассписание'},
        ),
        migrations.AlterModelOptions(
            name='typeoftraining',
            options={'verbose_name': 'Тип тренировки', 'verbose_name_plural': 'Типы тренировок'},
        ),
    ]
