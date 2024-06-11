from django.urls import path
from acostacesarapp import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
]