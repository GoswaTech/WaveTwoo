from django.urls import path

from . import views


urlpatterns = [
    path('snap_history/', views.snap_history, name='snap_history'),
]
