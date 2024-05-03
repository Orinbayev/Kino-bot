from django.urls import path
from .views import MovieViews



urlpatterns = [
    path('',MovieViews.as_view())
]