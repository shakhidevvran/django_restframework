from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie'.split()
