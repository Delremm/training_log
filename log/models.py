from django.db import models
from django.contrib.auth.models import User

class ExerciseBodypart(models.Model):
    bodypart_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.bodypart_name

class Exercise(models.Model):
    name = models.CharField(max_length=200)

    bodypart = models.ManyToManyField(ExerciseBodypart, related_name='bodyparts', null=True, blank=True)
    def __unicode__(self):
        return self.name

    #@models.permalink
    def get_absolute_url(self):
        return "/exercises/%s/" % self.id
        #return ('ExerciseDetailView', (), {'pk':str(self.id)})

    def to_dict(self):
        return {'exercise_name': self.name}



class Workout(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, null=True, blank=True)

    data = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.date.strftime("%A %d. %B %Y")

class Set(models.Model):
    exercise = models.ForeignKey(Exercise)
    workout = models.ForeignKey(Workout)

    def __unicode__(self):
        return 'set of %s, %s' % (self.exercise.name, self.workout.date.strftime("%A %d. %B %Y"))

class WeightRepsAbs(models.Model):
    weight = models.FloatField()
    reps = models.IntegerField()
    class Meta:
        abstract = True

#make extention of wrAbstract
class WeightReps(models.Model):
    weight = models.CharField(max_length=6)
    reps = models.IntegerField()
    set = models.ForeignKey(Set, related_name='weight_reps')
    def __unicode__(self):
        return 'weight: %s ,reps: %s' % (self.weight, self.reps)


gender_choices = (
    ('m', 'male'),
    ('f', 'female')
)

"""move height to checkout"""
class CommonPhysicalParams(models.Model):
    high = models.FloatField(null=True, blank=True)
    gender = models.CharField(choices=gender_choices, null=True, blank=True, max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User)

class CheckoutPhysicalParams(models.Model):
    date = models.DateField()
    weight_kg = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User)
    other_characteristics = models.TextField(null=True, blank=True)

"""add date, find out the difference between goal and checkpoint, if no merge them"""
class CheckPointMovement(WeightRepsAbs):
    exercise = models.ForeignKey(Exercise)

    def __unicode__(self):
        return "%s; weight:%s ,reps:%s"%(self.exercise, self.weight, self.reps)


class Goal(CheckPointMovement):
    date = models.DateField()
    user = models.ForeignKey(User)


class DayX(models.Model):
    exercises = models.ManyToManyField(Exercise)
    order = models.CharField(max_length=255)

    def get_exercises_in_order(self):
        exrcs = []
        for exrc_id in self.order.split(' '):
            exrcs.append(self.exercises.filter(id=int(exrc_id)))
        return exrcs

    def set_order(self, order):
        if isinstance(order, str):
            self.order = order
        else:
            pass


    def __unicode__(self):
        ret = ' '
        a = self.exercises.all()
        for n in self.exercises.all():

            ret += str(n)
        return ret


"""lot of to do, another app just like workouts"""
class Routine(models.Model):
    days = models.ManyToManyField(DayX)


"""it seems i got to use content_type, or even move to completely new app"""
class Achievement(models.Model):
    name = models.CharField(max_length=255)
    
class ExerciseImage(models.Model):
    image = models.ImageField(upload_to='media/img/exercise_images/', blank=True, null=True)
    exercise = models.ForeignKey(Exercise, related_name='images')

    def __unicode__(self):
        return self.exercise.name

from django.contrib import admin
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(Set)
admin.site.register(WeightReps)
admin.site.register(CommonPhysicalParams)
admin.site.register(CheckoutPhysicalParams)
admin.site.register(CheckPointMovement)
admin.site.register(Goal)
admin.site.register(ExerciseImage)
admin.site.register(DayX)
admin.site.register(Routine)
admin.site.register(ExerciseBodypart)