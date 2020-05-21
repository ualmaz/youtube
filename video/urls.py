from django.urls import include, path
from . import views
from .views import CalendarView, CalendarDetailView

app_name = 'video'

urlpatterns = [
    path('', views.home, name='home'),
    path('video/', views.video, name='video'),
    path('jquery', views.jQeryYouTube, name='jquery'),
    path('calendar/new/', views.calendar_form, name='calendar-form'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    # path('calendar/new/', CalendarCreateView.as_view(), name='calendar-form')


]
