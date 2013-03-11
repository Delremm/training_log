
from django.forms import ModelForm
from django import forms
from models import Workout, WeightReps, Goal, CheckPointMovement

class AddWorkoutForm(ModelForm):
    class Meta:
        model = Workout
        exclude = ('user')

class WeightRepsForm(forms.ModelForm):
    class Meta:
        model = WeightReps
        exclude = ['set']

    def save(self, *args, **kwargs):
        commit = False
        if kwargs.has_key('commit'):
            commit = kwargs['commit']
        WeightReps = super(WeightRepsForm, self).save(commit=False)
        if kwargs.has_key('set'):
            WeightReps.set = kwargs['set']
        if commit:
            WeightReps.save()
        return WeightReps

class AddGoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ['exercise', 'date', 'user']

    def save(self, *args, **kwargs):
        commit = False
        if kwargs.has_key('commit'):
            commit = kwargs['commit']
        Goal = super(AddGoalForm, self).save(commit=False)
        if 'exercise' and 'date' in kwargs:
            Goal.exercise = kwargs['exercise']
            Goal.date = kwargs['date']
        if commit:
            Goal.save()
        return Goal


class CheckPointForm(forms.ModelForm):
    class Meta:
        model = CheckPointMovement
        exclude = ['exercise']
