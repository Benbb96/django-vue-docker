from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from movie_review.models import Actor, Movie, Review
from movie_review.serializers import ActorSerializer, MovieSerializer, ReviewSerializer
from tasks import add_review


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 5


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = SmallResultsSetPagination


class ReviewViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer: ReviewSerializer):
        add_review.delay(**serializer.data)
