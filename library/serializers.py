from rest_framework import serializers

from .models import Books, Authors


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ("name",)


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, source='author_id')

    class Meta:
        model = Books
        fields = ("title", "published_year", "genre", "rating", "authors")

