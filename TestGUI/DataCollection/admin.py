from django.contrib import admin

from .models import TestConfiguration, Experiment

admin.site.register(TestConfiguration)
admin.site.register(Experiment)
# Register your models here.
