from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = ['',
               path(r'^$', TemplateView, {'template': 'karate.html'}, name='karate-home'),
               path(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='karate-event'),
               path(r'^swingtime/', include('swingtime.urls')),
               ]
