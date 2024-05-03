from rest_framework import serializers
from .models import MoviesModel

class MovieSer(serializers.ModelSerializer):
    class Meta:
        model = MoviesModel
        fields = "__all__"