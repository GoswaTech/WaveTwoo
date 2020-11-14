from django.urls import path

from . import views


urlpatterns = [
    path('cooktea/', views.cooktea_home, name="cooktea_home"),
    path('cooktea/cooktsu/<int:id>/', views.cooktea_cooktsu, name="cooktea_cooktsu"),
]
