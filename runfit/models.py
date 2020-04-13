from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="coach")
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to="coach_avatars/", blank=True)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return self.user.get_full_name()


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="person")
    # name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    avatar = models.ImageField(upload_to="person_avatars/", verbose_name="Аватар", blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.user.get_full_name()


class TypeOfTraining(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name="training_type")
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = "Тип тренировки"
        verbose_name_plural = "Типы тренировок"

    def __str__(self):
        return self.name


class Order(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    pick_training = models.ForeignKey(TypeOfTraining, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.id)


class TrainingSchedule(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    training_type = models.ForeignKey(TypeOfTraining, on_delete=models.CASCADE)
    start_at = models.DateTimeField()

    class Meta:
        verbose_name = "Рассписание"
        verbose_name_plural = "Рассписание"

    def __str__(self):
        return str(self.id)
