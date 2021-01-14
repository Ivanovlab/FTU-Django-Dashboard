from django.contrib import admin

from .models import TestConfiguration, Experiment, Result

admin.site.register(TestConfiguration)
admin.site.register(Experiment)
admin.site.register(Result)
# Register your models here.
