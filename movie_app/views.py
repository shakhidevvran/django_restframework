from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorsListSerializer, MoviesListSerializer, ReviewsListSerializer
from .models import Director, Movie, Review


@api_view(["GET"])
def directors_view(request):
    products = Director.objects.all()
    data = DirectorsListSerializer(products, many=True).data
    return Response(data=data)

@api_view(["GET"])
def movies_view(request):
    products = Movie.objects.all()
    data = MoviesListSerializer(products, many=True).data
    return Response(data=data)

@api_view(["GET"])
def reviews_view(request):
    products = Review.objects.all()
    data = ReviewsListSerializer(products, many=True).data
    return Response(data=data)