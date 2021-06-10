import operator
from datetime import datetime
from itertools import chain
from typing import Dict

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin,
                                   DestroyModelMixin)
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Books, Authors
from .serializers import BookSerializer, AuthorSerializer


class AuthorView(ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 GenericAPIView,
                 ViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer

    @action(methods=['GET'], detail=False, url_path='top', url_name='top')
    def get_top_authors(self, request):
        response = {}

        authors_ids = Authors.objects.values_list('id', flat=True)

        try:
            for i in range(len(authors_ids)):
                response[self.queryset.filter(id=authors_ids[i]).first().name] = \
                    Books.objects.all().filter(author_id=authors_ids[i]).count()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = dict(sorted(response.items(), key=operator.itemgetter(1), reverse=True)[:10])

        return Response(response)



class BookView(ListModelMixin,
               RetrieveModelMixin,
               DestroyModelMixin,
               GenericAPIView,
               ViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

    @action(methods=['GET'], detail=False, url_path='top', url_name='top')
    def get_top_books(self, request):
        queryset = self.get_queryset().order_by('-rating')
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='year', url_name='year')
    def get_year_books(self, request):
        try:
            body = request.query_params
            year_from = datetime(int(body.get("from")), 1, 1)
            year_to = datetime(int(body.get("to")), 12, 31)

            queryset = self.get_queryset().filter(published_year__gte=year_from, published_year__lte=year_to)
            serializer = self.get_serializer(queryset, many=True)

            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FindView(ListModelMixin,
               GenericAPIView,
               ViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        body:Dict = request.query_params

        try:
            if len(body) == 1:
                author_name = body.get("q")
                author_ids = Authors.objects.all().filter(name=author_name).first().id

                q = self.queryset.filter(author_id=author_ids)
            elif len(body) > 1:
                author_names = [body.get("q")]
                q = []

                for key in list(body.keys())[1:]:
                    author_names.append(key)

                for name in author_names:
                    q.append(self.queryset.filter(author_id=Authors.objects.all().filter(name=name).first().id))

                q = chain.from_iterable(set(q))
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
              
            serializer = self.get_serializer(q, many=True)
            
            return Response(serializer.data)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
          

class GenreView(ListModelMixin,
                GenericAPIView,
                ViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        genres:tuple = Books.objects.values_list('genre', flat=True)

        response = {}

        for i in range(len(genres)):
            response[genres[i]] = self.queryset.filter(genre=genres[i]).count()

        return Response(response)
