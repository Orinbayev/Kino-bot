from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MoviesModel
from .serializer import MovieSer


class MovieViews(ListAPIView):
    queryset = MoviesModel.objects.all()
    serializer_class = MovieSer



