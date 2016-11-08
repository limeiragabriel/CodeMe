from django.conf.urls import patterns, include, url
from . import views

#app_name = 'activitie'

urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'quiz/add/$', views.QuizCreate.as_view(), name='quiz-add'),
    url(r'quiz/(?P<pk>[0-9]+)/$', views.QuizUpdate.as_view(), name='quiz-update'),
    url(r'quiz/(?P<pk>[0-9]+)/delete/$', views.QuizDelete.as_view(), name='quiz-delete'),
)
