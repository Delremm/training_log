from django.contrib import admin

from log_app.models import Workout, Exercise, ExerciseBodypart

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(ExerciseBodypart)