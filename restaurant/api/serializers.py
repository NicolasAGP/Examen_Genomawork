from rest_framework import serializers
from restaurant.models import restaurant, Restauran_ubicacion


class RestaurantListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='restaurant_detail', read_only=True)

    class Meta:
        model = restaurant
        fields = ['id', 'name', 'description', 'Restauran_ubicacion', 'active',  'url']

class RestaurantDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = restaurant
        fields = ['id', 'name', 'description', 'active',  'tag_category']

class RestaurantubiListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='restaurant_ubi_detail', read_only=True)

    class Meta:
        model = Restauran_ubicacion
        fields = ['id', 'title', 'latitude', 'longitude', 'active',  'url']

class RestaurantubiDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restauran_ubicacion
        fields = ['id', 'title', 'latitude', 'longitude']
