from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'bet_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<bet_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<bet_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<bet_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^register/$', views.register, name='register'),
    url(r'^mybets/$', views.mybets, name='mybets'),

]
