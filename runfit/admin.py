from django.contrib import admin
from runfit.models import Coach, Person, TypeOfTraining, Order, TrainingSchedule

admin.site.register(Coach)
admin.site.register(Person)
admin.site.register(TypeOfTraining)
admin.site.register(TrainingSchedule)
admin.site.register(Order)
