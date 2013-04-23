from django.conf.urls import include, patterns, url
from log_app import views
from django.views import generic
from django.contrib.auth.decorators import login_required

from log_app.vkontakte import vkontakte_view

urlpatterns = patterns('',
    url(r'api/workouts/$', views.WorkoutListApi.as_view(), name='workouts'),
    url(r'api/workouts/(?P<pk>[0-9]+)/$', views.WorkoutDetailApi.as_view(), name='workouts'),
    url(r'api/workouts/(?P<date>(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01]))/$', views.WorkoutDetailApiDate.as_view(), name='workouts'),
    url(r'api/exercises/$', views.ExerciseListApi.as_view(), name='exercises'),
    url(r'api/exercises/(?P<pk>\d+)/$', views.ExerciseDetailApi.as_view(), name='exercises'),
    url(r'api/workouts_s/$', views.WorkoutsWithExerciseNamesApi.as_view(), name='workouts_s'),

    url(r'workouts/$', views.WorkoutListView.as_view(), name='workouts'),
    url(r'add_workout/$', login_required(generic.TemplateView.as_view(template_name='log_app/add_workout.html')), name="add_workout"),
    url(r'vk/$', vkontakte_view, name='vk_app'),
    url(r'$', login_required(generic.TemplateView.as_view(template_name='log_app/index.html')), name='index'),
)