
from datetime import date
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class ExerciseBodypart(models.Model):
    bodypart_name = models.CharField(_("name of body part"), max_length=255)

    def __unicode__(self):
        return self.bodypart_name


class Exercise(models.Model):
    name = models.CharField(_("name of the exercise"), max_length=200)

    #1-weight, 2-running, 3-sprint, 4-boxing
    type = models.IntegerField(_("type of exercise"))

    bodypart = models.ManyToManyField(ExerciseBodypart, related_name='bodyparts', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    #@models.permalink
    def get_absolute_url(self):
        return "/log/exercises/%s/" % self.id
        #return ('ExerciseDetailView', (), {'pk':str(self.id)})

import json
import ast


class Workout(models.Model):
    date = models.DateField(_("date"), default=date.today())

    user = models.ForeignKey(User, related_name='workouts', null=True, blank=True)

    data = models.TextField(null=True, blank=True, verbose_name=_("data"))

    def save(self, force_insert=False, force_update=False, using=None):
        a = ast.literal_eval(self.data)
        a = json.dumps(a)
        self.data = a
        super(Workout, self).save()

    def __unicode__(self):
        return self.date.strftime("%A %d. %B %Y")


class Set(models.Model):
    exercise = models.ForeignKey(Exercise)
    data = models.TextField(null=True, blank=True)
    workout = models.ForeignKey(Workout, related_name='sets')

    def __unicode__(self):
        return self.data + self.exercise.name
