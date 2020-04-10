from django.contrib import admin
from runfit.models import Coach, Person, TypeOfTraining, Order, TrainingSchedule

admin.site.site_header = "Административная панель RunFit"


@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
    list_display = ('coach', 'training_type', 'start_at')
    list_filter = ('coach', 'training_type', 'start_at')


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'name', 'phone', 'get_email')
    list_filter = ('name',)

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_email(self, obj):
        return obj.user.email


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'phone', 'get_email')

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_email(self, obj):
        return obj.user.email


@admin.register(TypeOfTraining)
class TypeOfTrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('person', 'coach', 'total', 'pick_training', )
    list_filter = ('pick_training', 'total')
