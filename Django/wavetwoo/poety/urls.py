from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.poety_menu, name='poety_home'),
    path('snap_history/<slug:slug>/', views.snap_history, name='snap_history'),
]
