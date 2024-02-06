from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from api.models import Movie
from api.serializers import UserSerializer, MovieSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.filter(after_premiere=True)
