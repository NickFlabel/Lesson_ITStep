from rest_framework import serializers
from .models import Author, Location, Publisher, Book

from django.shortcuts import get_object_or_404


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    birthdate = serializers.DateField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()
        return instance

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

class AuthorUpdateSerializer(AuthorSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=False)
    birthdate = serializers.DateField(required=False)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Имя должно быть больше трех символов')
        return value


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'



