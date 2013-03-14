from django.views import generic

from log_app.models import Workout, Exercise
from log_app.serializers import WorkoutSerializer, ExerciseSerializer, UserSerializer
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, JSONPRenderer, BrowsableAPIRenderer
from rest_framework import authentication, permissions
import json


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """
    
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated():
            return True
        return False
	
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class WorkoutListApi(generics.ListCreateAPIView):
    model = Workout
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class WorkoutDetailApi(generics.RetrieveUpdateDestroyAPIView):
    model = Workout
    serializer_class = WorkoutSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class WorkoutDetailApiDate(generics.RetrieveUpdateDestroyAPIView):
    model = Workout
    serializer_class = WorkoutSerializer
    permission_classes = (IsOwner, )
    slug_field = 'date'
    slug_url_kwarg = 'date'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class ExerciseListApi(generics.ListAPIView):
    model = Exercise
    serializer_class = ExerciseSerializer


class ExerciseDetailApi(generics.RetrieveAPIView):
    model = Exercise
    serializer_class = ExerciseSerializer


class WorkoutListView(generic.ListView):
    template_name = 'log_app/workouts.html'
    model = Workout





#delete


class WorkoutsWithExerciseNamesApi(APIView):


    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        workouts = Workout.objects.all()
        workouts_s = WorkoutSerializer(workouts)
        print 'workouts_s: '
        print workouts_s.data
        ilist = []
        jlist = []
        for i in workouts_s.data:
            print 'gg:'
            print i['data']
            ilist.append([])
            for j in json.loads(i['data']):
                print 'ss: '
                print j
                try:
                    exrc = Exercise.objects.get(id=j[0])
                except Exercise.DoesNotExist:
                    return Response('')
                else:
                    j[0] = [j[0], exrc.name]
                    print j[0]
                    ilist[-1].append(j)
                    print "eee"
                    print ilist[-1]
            jlist.append(ilist)
            ilist = []

        return Response(jlist)
