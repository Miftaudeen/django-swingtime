from django.urls import path

from swingtime import views

urlpatterns = ['',
               path(r'^(?:calendar/)?$',
                    view=views.today_view,
                    name='swingtime-today'),

               path(r'^calendar/(?P<year>\d{4})/$',
                    view=views.year_view,
                    name='swingtime-yearly-view'),

               path(r'^calendar/(\d{4})/(0?[1-9]|1[012])/$',
                    view=views.month_view,
                    name='swingtime-monthly-view'),

               path(r'^calendar/(\d{4})/(0?[1-9]|1[012])/([0-3]?\d)/$',
                    view=views.day_view,
                    name='swingtime-daily-view'),

               path(r'^events/$',
                    view=views.event_listing,
                    name='swingtime-events'),

               path(r'^events/add/$',
                    view=views.add_event,
                    name='swingtime-add-event'),

               path(r'^events/(\d+)/$',
                    view=views.event_view,
                    name='swingtime-event'),

               path(r'^events/(\d+)/(\d+)/$',
                    view=views.occurrence_view,
                    name='swingtime-occurrence')
               ]
