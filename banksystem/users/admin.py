from django.contrib import admin
from django_celery_beat.models import PeriodicTask

from .models import User

admin.site.register(User)


class PeriodicTaskAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(PeriodicTask)
admin.site.register(PeriodicTask, PeriodicTaskAdmin)
