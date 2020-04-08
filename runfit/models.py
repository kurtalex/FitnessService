from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="coach")
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to="coach_avatars/", blank=False)

    def __str__(self):
        return self.user.get_full_name()


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="person")
    # name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="person_avatars/", blank=False)

    def __str__(self):
        return self.user.get_full_name()


class TypeOfTraining(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name="training_type")
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    FITNESS = 1
    AEROBICS = 2
    GYMNASTICS = 3
    PILATES = 4
    WEIGHT_LOSS = 5
    YOGA = 6
    CROSSFIT = 7
    SPINNING = 8

    TYPE_OF_TRAINING_CHOICES = (
        (FITNESS, "Фитнес"),
        (AEROBICS, "Аэробика"),
        (GYMNASTICS, "Гимнастика"),
        (PILATES, "Пилатес"),
        (WEIGHT_LOSS, "Жиросжигание"),
        (YOGA, "Йога"),
        (CROSSFIT, "Кроссфит"),
        (SPINNING, "Спиннинг")
    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    total = models.IntegerField()
    pick_training = models.IntegerField(choices=TYPE_OF_TRAINING_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class TrainingSchedule(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    training_type = models.ForeignKey(TypeOfTraining, on_delete=models.CASCADE)
    start_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)
