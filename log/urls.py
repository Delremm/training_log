from django.conf.urls import include, patterns, url

from log.views import WorkoutsView, WorkoutDetailView, ChoiceExerciseView, WeightRepsAddView, WorkoutDeleteView,\
    ExerciseChangeView, WeightRepsChangeView, GoalsView, GoalChoiceExrc, AddGoalView, GoalDeleteView, CommonPhysicalParamsView,\
    CommonPhysPramsListView, CheckPointListView, CheckPointChoiceExrc, CheckPointAdd, CheckPointDeleteView, ExercisesView,\
    ExerciseDetailView, IndexView, WorkoutSetDeleteView
from log import views

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
    (r'^exercises/$', ExercisesView.as_view()),
    (r'^exercises/(?P<pk>\d+)/$', ExerciseDetailView.as_view()),
    (r'^workouts/$', WorkoutsView.as_view()),
    (r'^workouts/(?P<pk>\d+)/$', WorkoutDetailView.as_view()),
    (r'^workouts/(?P<pk>\d+)/del/$', WorkoutDeleteView.as_view()),
    (r'^workouts/(?P<pk>\d+)/set_del/$', WorkoutSetDeleteView.as_view()),
    (r'^choice_exercise/$', ChoiceExerciseView.as_view()),
    (r'^exercise_change/$', ExerciseChangeView.as_view()),
    (r'^weight_reps_add/$', WeightRepsAddView.as_view()),
    (r'^weight_reps_change/$', WeightRepsChangeView.as_view()),
    (r'^goals/$', GoalsView.as_view()),
    (r'^goals/goal_exrc_choice/$', GoalChoiceExrc.as_view()),
    (r'^goals/add_goal/$', AddGoalView.as_view()),
    (r'^goals/(?P<pk>\d+)/del/$', GoalDeleteView.as_view()),
    (r'^common_params/$', CommonPhysPramsListView.as_view()),
    (r'^common_params_detail/$', CommonPhysicalParamsView.as_view()),
    (r'^check_points/$', CheckPointListView.as_view()),
    (r'^check_points/check_point_exrc_choice/$', CheckPointChoiceExrc.as_view()),
    (r'^check_points/add/$', CheckPointAdd.as_view()),
    (r'^check_points/(?P<pk>\d+)/del/$', CheckPointDeleteView.as_view()),
)


"""

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gg.views.home', name='home'),
    # url(r'^gg/', include('gg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^$', EntryView.as_view()),
    (r'exercises/$', ExercisesView.as_view()),
    (r'exercises/(?P<pk>\d+)/$', ExerciseDetailView.as_view()),
    (r'^workouts/$', WorkoutsView.as_view()),
    (r'^workouts/(?P<pk>\d+)/$', WorkoutDetailView.as_view()),
    (r'^workouts/(?P<pk>\d+)/del/$', WorkoutDeleteView.as_view()),
    (r'^choice_exercise/$', ChoiceExerciseView.as_view()),
    (r'^exercise_change/$', ExerciseChangeView.as_view()),
    (r'^weight_reps_add/$', WeightRepsAddView.as_view()),
    (r'^weight_reps_change/$', WeightRepsChangeView.as_view()),
    (r'^goals/$', GoalView.as_view()),
    (r'^goals/goal_exrc_choice/$', GoalChoiceExrc.as_view()),
    (r'^goals/add_goal/$', AddGoalView.as_view()),
    (r'^goals/(?P<pk>\d+)/del/$', GoalDeleteView.as_view()),
    (r'^common_params/$', CommonPhysPramsListView.as_view()),
    (r'^common_params_detail/$', CommonPhysicalParamsView.as_view()),
    (r'^check_points/$', CheckPointListView.as_view()),
    (r'^check_points/check_point_exrc_choice/$', CheckPointChoiceExrc.as_view()),
    (r'^check_points/add/$', CheckPointAdd.as_view()),
    (r'^check_points/(?P<pk>\d+)/del/$', CheckPointDeleteView.as_view()),
    (r'^test/$', TestView.as_view()),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

"""