from django.conf.urls import patterns
from views import EntryView, PostDetailView, NewPostView
urlpatterns = patterns('',
    (r'^index/$', EntryView.as_view()),
    (r'^(?P<pk>\d+)', PostDetailView.as_view()),
    (r'^new_post/$', NewPostView.as_view()),
)