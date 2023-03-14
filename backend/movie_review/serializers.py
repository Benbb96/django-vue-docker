from rest_framework import serializers

from movie_review.models import Actor, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'grade', 'movie']


class GradeListingField(serializers.RelatedField):
    """ Create custom RelatedField in order to list all grade reviews as integer in MovieSerializer """
    def to_internal_value(self, data):
        pass

    def to_representation(self, review: Review):
        return review.grade


class MovieSerializer(serializers.ModelSerializer):
    review_set = GradeListingField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'review_set']
