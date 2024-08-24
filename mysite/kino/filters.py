from django_filters.rest_framework import FilterSet
from .models import Movie, Rating


class Moviefilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country': ['exact'],
            'genre': ['exact'],
            'date': ['gt', 'lt'],
        }


class Ratingfilter(FilterSet):
    class Meta:
        model = Rating
        fields = {
            'stars': ['gt', 'lt']
        }

from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    return len(value) == int(arg)