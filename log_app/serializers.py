from django.forms import widgets
from rest_framework import serializers
from log_app.models import Workout, Exercise

import ast
import json


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'date', 'data', 'user')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.date = attrs.get('date', instance.date)
            instance.data = attrs.get('data', instance.data)
            #instance.user = attrs.get('user', instance.user)
            return instance
        # Create new instance
        return Workout(**attrs)


class ExerciseSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField(max_length=200)
    type = serializers.IntegerField()
    description = serializers.CharField(widget=widgets.Textarea, max_length=5000)
    bodypart = serializers.RelatedField(many=True, read_only=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.name = attrs.get('name', instance.name)
            instance.type = attrs.get('type', instance.type)
            instance.description = attrs.get('description', instance.description)
            return instance
        return Exercise(**attrs)


class SetSerializer(serializers.Serializer):
    pk = serializers.Field()
    exercise = serializers.Field()
    data = serializers.CharField(widget=widgets.Textarea, max_length=5000)
    workout = serializers.Field()


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    workout_set = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'workout_set')