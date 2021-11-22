from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework import generics, permissions , filters
from restaurant.models import restaurant, Restauran_ubicacion
from .serializers import RestaurantListSerializer,RestaurantDetailSerializer,RestaurantubiListSerializer,RestaurantubiDetailSerializer


class RestaurantListAPIView(generics.ListCreateAPIView):
    serializer_class = RestaurantListSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = restaurant.objects.filter(active=True)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('Restauran_ubicacion',)
    search_fields = ['name', 'tag_category']


class RestaurantDetailAPIView(generics.RetrieveAPIView):
    serializer_class = RestaurantDetailSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = restaurant.objects.filter(active=True)

class RestaurantubiListAPIView(generics.ListCreateAPIView):
    serializer_class = RestaurantubiDetailSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = Restauran_ubicacion.objects.filter(active=True)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ()
    search_fields = ['title', 'tag_category']


class RestaurantubiDetailAPIView(generics.RetrieveAPIView):
    serializer_class = RestaurantubiListSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = Restauran_ubicacion.objects.filter(active=True)
