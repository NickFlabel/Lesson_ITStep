from rest_framework import serializers
from .models import Author, Location, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']


class PublisherSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Publisher
        fields = '__all__'
