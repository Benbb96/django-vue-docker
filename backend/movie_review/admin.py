from django.contrib import admin

from movie_review.models import Actor, Movie, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')


@admin.register(Movie)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    autocomplete_fields = ('actors',)


@admin.register(Review)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade', 'movie')
    list_filter = ('grade',)
    search_fields = ('movie__title',)
